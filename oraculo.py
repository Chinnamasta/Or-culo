import tempfile
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from loaders import *

st.set_page_config(page_title="Oráculo IA", layout="wide")
st.header('🔮 Bem-vindo ao Oráculo!')

TIPOS_ARQUIVOS_VALIDOS = ['site', 'youtube', 'pdf', 'csv', 'txt']

CONFIG_MODELOS = {
    'OpenAI': {
        'modelos': ['gpt-4o-mini', 'gpt-4o'],
        'chat': ChatOpenAI
    }
}

MEMORIA = ConversationBufferMemory()
MEMORIA.chat_memory.add_user_message('Olá IA!')
MEMORIA.chat_memory.add_ai_message('Olá humano!')

def carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo):
    documento = None

    if tipo_arquivo == 'site' and arquivo:
        documento = carrega_site(arquivo)
    elif tipo_arquivo == 'youtube' and arquivo:
        documento = carrega_youtube(arquivo)
    elif tipo_arquivo in ['pdf', 'csv', 'txt'] and arquivo:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            temp.write(arquivo.read())
            nome_temp = temp.name
        if tipo_arquivo == 'pdf':
            documento = carrega_pdf(nome_temp)
        elif tipo_arquivo == 'csv':
            documento = carrega_csv(nome_temp)
        elif tipo_arquivo == 'txt':
            documento = carrega_txt(nome_temp)

    if documento:
        st.subheader("📄 Conteúdo carregado:")
        for i, doc in enumerate(documento):
            with st.expander(f"Trecho {i+1}", expanded=(i == 0)):
                st.markdown(doc.page_content if hasattr(doc, "page_content") else str(doc))
    else:
        st.warning('Nenhum conteúdo foi carregado.')

    chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat
    st.session_state['memoria'] = MEMORIA


def sidebar():
    tabs = st.tabs(['📂 Upload de Arquivos', '⚙️ Seleção de Modelos'])

    with tabs[0]:
        tipo_arquivo = st.selectbox('Tipo de conteúdo', TIPOS_ARQUIVOS_VALIDOS)
        arquivo = None
        if tipo_arquivo == 'site':
            arquivo = st.text_input('Digite a URL do site')
        elif tipo_arquivo == 'youtube':
            arquivo = st.text_input('Digite a URL do vídeo do YouTube')
        elif tipo_arquivo in ['pdf', 'csv', 'txt']:
            arquivo = st.file_uploader('Faça o upload do arquivo', type=[tipo_arquivo])

    with tabs[1]:
        provedor = st.selectbox('Provedor do modelo', CONFIG_MODELOS.keys())
        modelo = st.selectbox('Modelo', CONFIG_MODELOS[provedor]['modelos'])
        api_key = st.text_input(f'API Key do {provedor}', type='password')

        st.session_state[f'api_key_{provedor}'] = api_key

    if st.button('🔁 Inicializar Oráculo', use_container_width=True):
        if not arquivo:
            st.warning("Por favor, insira ou envie um conteúdo para continuar.")
        elif not api_key:
            st.warning("A API Key é obrigatória.")
        else:
            carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo)


with st.sidebar:
    sidebar()

# Renderiza o chat se o modelo já foi carregado
if 'chat' in st.session_state:
    chat_model = st.session_state['chat']
    memoria = st.session_state.get('memoria', MEMORIA)

    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    input_usuario = st.chat_input('Fale com o Oráculo')
    if input_usuario:
        memoria.chat_memory.add_user_message(input_usuario)
        st.chat_message('human').markdown(input_usuario)

        resposta = chat_model.invoke(input_usuario).content
        st.chat_message('ai').markdown(resposta)

        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria
