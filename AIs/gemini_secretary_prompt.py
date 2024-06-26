import google.generativeai as genai
from datetime import date
from docx import Document
import os


def extrair_procedimento(filename: str):
    try:
        doc = Document(filename)
        texto = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        texto = ''
        print(e)

    return texto


genai.configure(api_key=os.environ['GEMINI_API_KEY'])

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
    system_instruction="""Sou assistente de secretária do time de PCP da WEG Energia."""
)


class SecretaryAI:
    def __init__(self):
        self.chat_session = model.start_chat()

    def send_message(self, path: str, filename: str):
        message = f"""
        Procedimento sobre {filename}:
        {extrair_procedimento(f'{path}')}
        Fim do procedimento;

        Baseado nas informações do procedimento acima, realize os comandos abaixo:

        FAÇA essas alterações com os textos entre aspas quando aparecerem no procedimento acima:
        Caso esteja escrito "ANO_ATUAL" Substitua "ANO_ATUAL" por {date.today().year}, 
        Caso esteja escrito "MES_ATUAL" Substitua "MES_ATUAL" por {date.today().month:02}, 
        Caso esteja escrito "SEMANA_ATUAL" Substitua "SEMANA_ATUAL" por {date.today().isocalendar().week}, 
        Caso esteja escrito "DIA_ATUAL" Substitua "DIA_ATUAL" por {date.today().day:02}
        Caso esteja escrito "SEM_PASSADO" Substitua "SEM_PASSADO" por {str(int(date.today().strftime('%m')) - 1).zfill(2)}; Caso esteja escrito "LastUpdate" Formate as datas de 'LastUpdate' do procedimento em formato de 'dd/mm/yyyy', mantendo a mesma data.
        
        Separe o passo a passo para atualizar o indicador em vários tópicos;
"""
        response = self.chat_session.send_message(message).text
        return response.strip()


if __name__ == "__main__":
    procedure_path = ("Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\PPC_AI_Procedures\\ppc_secretary\\daily\\Kanban diário "
                      "JGS.docx")
    procedure_name = "Kanban diário JGS"
    ia = SecretaryAI()
    print(ia.send_message(procedure_path, procedure_name))
