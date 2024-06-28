from Indicators.get_data import atualizar_stocks, atualizar_atendimento_ov, mesclar_dados
from functions import input_history

from AIs.gemini_chatbot import GeminiAI
from AIs.gemini_search_folders import SearchFoldersAI
from AIs.gemini_secretary_prompt import SecretaryAI

import json
user_ias = {}


def process_message_function(request):
    message = request.form.get('message')
    if not message:
        return "Mensagem inválida", 400

    username = request.form.get('username')
    if 'SITE' in username:
        username = request.remote_addr

    if username not in user_ias:
        user_ias[username] = GeminiAI()

    response = user_ias[username].send_message(message)

    try:
        input_history(username, message, response)
    except Exception as e:
        print(str(e))

    return response


def quit_system_function(request):
    username = request.form.get('username')
    if 'SITE' in username:
        username = request.remote_addr
    try:
        del user_ias[username]
        return f'Usuário {username} deletado com sucesso!'
    except KeyError:
        return 'Usuário inexistente'
    except Exception as e:
        print(str(e))
        return 'Ocorreu um erro ao deletar o usuário.'


def search_file_function(request):
    message = request.form.get('message')
    if not message:
        return "Mensagem inválida", 400

    search = SearchFoldersAI()
    return search.send_message(message)


def search_secretary_procedure_function(request):
    path = request.form.get('path')
    filename = request.form.get('filename')

    if not filename:
        return "Nome de arquivo inválido", 400

    search = SecretaryAI()
    return search.send_message(path, filename)


def get_json_file(filename: str):
    try:
        return json.load(open(filename, "r", encoding="utf-8"))
    except Exception as e:
        print(str(e))
        return []

def update():
    try:
        atualizar_stocks()
        atualizar_atendimento_ov()
        mesclar_dados()
        return True

    except Exception as e:
        print(str(e))
        return False


update()
