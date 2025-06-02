from langchain_community.document_loaders import (
    WebBaseLoader, YoutubeLoader, CSVLoader, PyPDFLoader, TextLoader
)

# ---- Função para carregar conteúdo de um site
def carrega_site(url):
    loader = WebBaseLoader(url)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# ---- Função para carregar transcrição de vídeo do YouTube
def carrega_youtube(video_id):
    try:
        loader = YoutubeLoader(video_id, add_video_info=False, language=['pt'])
        lista_documentos = loader.load()
        documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
        return documento
    except Exception as e:
        print(f"[Erro ao carregar vídeo {video_id}] {e}")
        return ""  # retorna string vazia para não quebrar o código

# ---- Função para carregar um arquivo CSV
def carrega_csv(caminho):
    loader = CSVLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# ---- Função para carregar PDF
def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

# ---- Função para carregar arquivos TXT
def carrega_txt(caminho):
    loader = TextLoader(caminho, encoding='utf-8')
    lista_documentos = loader.load()
    documento = '\n\n'.join([doc.page_content for doc in lista_documentos])
    return documento

