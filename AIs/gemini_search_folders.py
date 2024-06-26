import google.generativeai as genai
from AIs.data_search_folders import historico
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
)

arquivos = open(
    'Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Central\\__Automaticos_Python\\06-find_fles\\database\\all.txt', 'r',
    encoding="utf-8").read()


class SearchFoldersAI:
    def __init__(self):
        self.chat_session = model.start_chat(
            history=historico
        )

    def send_message(self, descricao: str):
        message = f"""{arquivos}
    Ordene os tópicos de acordo com o número de seu Score, de maior para menor;
    Faça essa análise se baseando na descrição a seguir: {descricao}; Analisando todos os arquivos acima quero que 
    crie um ranking dos 5 arquivos que mais tem relação com a descrição desejada (NÃO MOSTRE NADA ALÉM DESSES 5 
    ARQUIVOS); Avalie de acordo com as extensões abaixo: - Macros do Excel: arquivos com extensão .xlsm; - Arquivos 
    de texto: arquivos com extensão .txt; - Arquivos Power BI: arquivos com extensão .pbix; etc.
    
    Faça essa análise se baseando nos critérios de avaliação abaixo:
    - O nome das pastas que os arquivos se encontram tem relação com a descrição passada como parâmetro? (score máximo: 30/100);
    - A pasta do arquivo tem um mapeamento que condiz com a descrição passada como parâmetro? (score máximo: 20/100);
    - Os nomes dos arquivos tem relação com a descrição passada como parâmetro? (score máximo: 20/100);
    - Baseado no histórico de perguntas, a descrição passada como parâmetro condiz com alguma resposta anterior? (score máximo: 15/100);
    - A última data de atualização é recente? (score máximo: 15/100);

    Crie um tópico para cada arquivo, mostrando o caminho EXATO do arquivo, dentro desse tópico crie alguns subtópicos: 
    -Explique o motivo pelo posicionamento;
    -Nome do arquivo;
    -Última data de atualização;
    -Score que o arquivo atingiu;
    """
        response = self.chat_session.send_message(message).text
        return response.strip()


if __name__ == "__main__":
    ia = SearchFoldersAI()
    resumo = ia.send_message('Kanban Diário')
    print(resumo)
