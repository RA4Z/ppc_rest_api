from extract import extrair_info
import json
import os

path_daily = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/PPC_AI_Procedures/ppc_secretary/daily'
path_weekly = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/PPC_AI_Procedures/ppc_secretary/weekly'
path_monthly = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/PPC_AI_Procedures/ppc_secretary/monthly'
path_rules = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/PPC_AI_Procedures/rules'
path_docs = 'Q:/GROUPS/BR_SC_JGS_WM_LOGISTICA/PCP/PPC_AI_Procedures/documents'

path_procedures = '\\\\intranet.weg.net@SSL\\DavWWWRoot\\br\\energia-wm\\pcp\\Central de Arquivos'
path_pcr = '\\\\intranet.weg.net@SSL\\DavWWWRoot\\br\\energia-wm\\pcp\\PCR'

default_answers = json.load(open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\PPC_AI_Procedures\\documents'
                                 '\\default_answers.json', 'r', encoding='utf-8'))
pathsPCP = json.load(
    open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\PPC_AI_Procedures\\documents\\Links_Uteis.json', 'r',
         encoding='utf-8'))
agendaPCP = json.load(
    open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\PPC_AI_Procedures\\documents\\agenda.json', 'r', encoding='utf-8'))
transacoesWEG = json.load(open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\PPC_AI_Procedures\\documents\\TRANSAÇÕES-WEG'
                               '.json', 'r', encoding='utf-8'))

paths = [path_daily, path_weekly, path_monthly, path_procedures, path_pcr]
historico = []

# INSERIR INFORMAÇÕES DA AGENDA DO PCP, CRIADA PELA MARGUIT
for path in pathsPCP:
    historico.append({
        "role": "user",
        "parts": [
            f"Links do {path['filename']}"
        ]
    })
    historico.append({
        "role": "model",
        "parts": [
            f"Link da Web: {path['web_path']}\nPasta da Rede: {path['groups_path']}"
        ]
    })

for transacao in transacoesWEG:
    historico.append({
        "role": "user",
        "parts": [
            f"Transação {transacao['Transação']}"
        ]
    })
    historico.append({
        "role": "model",
        "parts": [
            f"{transacao['Transação']}: {transacao['Título da Transação']}"
        ]
    })

# INSERIR INFORMAÇÕES DA AGENDA DO PCP, CRIADA PELA MARGUIT
for seq in agendaPCP:
    historico.append({
        "role": "user",
        "parts": [
            f"Agenda PCP Sequência {seq['SEQ']}:"
        ]
    })
    historico.append({
        "role": "model",
        "parts": [
            f"\nSequência: {seq['SEQ']}\n{seq['REFERÊNCIA']}\nDescrição: {seq['DESCRIÇÃO']}\nUtilidade: {seq['UTILIDADE']}" +
            (f"\nDetalhes: {seq['DETALHES']}" if 'DETALHES' in seq else "")
        ]
    })

# NORMAS TRANSCRITAS
for filename in os.listdir(path_rules):
    if filename.endswith(".docx") or filename.endswith(".pdf"):
        historico.append({
            "role": "user",
            "parts": [
                f"Texto em extenso para a Norma {filename.replace('.docx', '').replace('.pdf', '')}"
            ]
        })
        historico.append({
            "role": "model",
            "parts": [
                extrair_info(f'{path_rules}/{filename}'),
            ]
        })

# DOCUMENTOS PCP
for filename in os.listdir(path_docs):
    if filename.endswith(".docx") or filename.endswith(".pdf"):
        historico.append({
            "role": "user",
            "parts": [
                f"Documento em extenso sobre {filename.replace('.docx', '').replace('.pdf', '')}"
            ]
        })
        historico.append({
            "role": "model",
            "parts": [
                extrair_info(f'{path_docs}/{filename}'),
            ]
        })

# INSERIR PROCEDIMENTOS E DOCUMENTOS WORD
for path in paths:
    for filename in os.listdir(path):
        if filename.endswith(".docx") or filename.endswith(".pdf"):
            historico.append({
                "role": "user",
                "parts": [
                    f"Procedimento em extenso para {filename.replace('.docx', '').replace('.pdf', '')}"
                ]
            })
            historico.append({
                "role": "model",
                "parts": [
                    f"{extrair_info(f'{path}/{filename}')} o procedimento se encontra em {path}/{filename}",
                ]
            })

for command in default_answers:
    historico.append({
        "role": "user",
        "parts": [
            command['input']
        ]
    })
    historico.append({
        "role": "model",
        "parts": [
            command['output']
        ]
    })
