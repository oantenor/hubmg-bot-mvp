import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key)

def ask_bot(message, history):
    return llm.invoke(message).content

chat = gr.ChatInterface(
        ask_bot,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Pergunte algo sobre para o HubMG Bot!", container=False, scale=7),
        title="HubMG Bot",
        description="Nosso bot está preparado para atender todas as suas dúvidas sobre licenciamento ambiental",
        theme="soft",
        examples=["Tenho uma padaria. Minha atividade é licenciável?", "Quais documentos preciso para obter o licenciamento?"],
        cache_examples=True,
        retry_btn=None,
        undo_btn=None,
        submit_btn="Enviar",
        clear_btn="Limpar",
    )

chat.launch(share=True, server_name="0.0.0.0", server_port=7860)