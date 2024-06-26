import google.generativeai as genai
from AIs.data_chatbot import historico
import os

genai.configure(api_key=os.environ['GEMINI_API_KEY'].strip())

generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="""Sou assistente do time de PCP da WEG Energia. Responderei às perguntas do usuário com base 
    em minhas informações. Caso a informação não esteja no meu contexto responderei: 'Desculpe,😞<br> me perdi no 
    raciocínio...😭<br> Poderia reformular a sua pergunta?😅"""
)


class GeminiAI:
    def __init__(self):
        self.chat_session = model.start_chat(
            history=historico
        )

    def send_message(self, message: str):
        message = f"""
    Reponda no idioma no qual está escrito: {message} 
    """
        response = self.chat_session.send_message(message).text
        return response.strip()


if __name__ == "__main__":
    ia = GeminiAI()
    resumo = ia.send_message('Nome do job que salva um arquivo de texto chamado KANBA_VESTAS_JGS.txt')
    print(resumo)
