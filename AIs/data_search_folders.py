import json

historico = [
    {
      "role": "user",
      "parts": [
        "O que significa EM?",
      ]
    },
    {
      "role": "model",
      "parts": ["EM/WEM é a filial da WEG, que se encontra nos Estados Unidos, normalmente(nem sempre) os arquivos "
                "relacionados a ela estão com o nome em inglês"]
    },
]

mapeamento = json.load(open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Central\\__Automaticos_Python\\06-find_fles'
                            '\\mapeamento.json', 'r', encoding='utf-8'))
inteligence = json.load(open('Q:\\GROUPS\\BR_SC_JGS_WM_LOGISTICA\\PCP\\Central\\__Automaticos_Python\\06-find_fles'
                             '\\inteligence.json', 'r', encoding='utf-8'))


for item in mapeamento:
    historico.append({
        "role": "user",
        "parts": [
            f"Qual o mapeamento da pasta {item['Folder']}?"
        ]
    })
    historico.append({
        "role": "model",
        "parts": f"Na pasta {item['Folder']} se encontram {[item['Content']]}"
    })


for item in inteligence:
    historico.append({
        "role": "user",
        "parts": [
            f"Histórico de perguntas: {item['Question']}"
        ]
    })
    historico.append({
        "role": "model",
        "parts": f"Baseado na descrição {item['Question']}, o arquivo {item['Answer']} é o correto."
    })

    