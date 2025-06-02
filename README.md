# 🔮 Projeto Oráculo

O **Oráculo** é uma aplicação web interativa desenvolvida em **Streamlit** com integração ao **LangChain**, que permite conversar com diferentes fontes de dados, como:

- Vídeos do YouTube
- Sites
- Arquivos PDF, CSV e TXT

Você escolhe o tipo de dado, faz o upload ou fornece a URL, e o Oráculo responde perguntas com base nesse conteúdo. O projeto oferece integração com **modelos de linguagem da OpenAI**.

## 🚀 Funcionalidades

- Interface web intuitiva com sidebar para seleção de fontes e modelos
- Suporte a múltiplos tipos de arquivos e URLs
- Memória de conversa com histórico visível no frontend
- Respostas contextualizadas baseadas no conteúdo fornecido

## 🧠 Tecnologias

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- Python

## 📦 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/projeto-oraculo.git
   cd projeto-oraculo

   pip install -r requirements.txt
   streamlit run app.py

