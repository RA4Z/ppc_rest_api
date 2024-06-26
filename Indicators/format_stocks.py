import datetime
import json

target_year = int((datetime.date.today() - datetime.timedelta(days=datetime.date.today().day)).strftime("%Y"))
replace_list = json.load(open("Indicators/replace_list.json", "r", encoding="utf-8"))

itens = []
for item in replace_list:
    if "Stocks" in item["actual"]:
        itens.append(item['actual'].replace('Stocks ', ''))


def replace_strings(actual: str, turns: bool):
    for item in replace_list:
        if item["actual"] == actual:
            if not turns:
                return f'{item["new"]}*'
            else:
                return f'{item["new"]} Turns'
    return None


def delete_months(item):
    del item['Jan']
    del item['Feb']
    del item['Mar']
    del item['Apr']
    del item['May']
    del item['Jun']
    del item['Jul']
    del item['Aug']
    del item['Sep']
    del item['Oct']
    del item['Nov']
    del item['Dec']


def formatar_json(data):
    formatted_data = []
    for item in data:
        for item_base in itens:
            if (item['Concatenar'] == f"{item_base}{target_year}Inventory"
                    or item['Concatenar'] == f"{item_base}{target_year}Inventory Turns"):  # Comparar com a chave "item"

                if "Turns" in item['Concatenar']:
                    turns = True
                else:
                    turns = False

                new = replace_strings(f"Stocks {item_base}", turns)
                if new is not None:
                    item['Concatenar'] = new

                item['averages'] = []
                item['data'] = [item['Jan'], item['Feb'], item['Mar'], item['Apr'], item['May'], item['Jun'],
                                item['Jul'], item['Aug'], item['Sep'], item['Oct'], item['Nov'], item['Dec']]
                delete_months(item)

                item['last'] = [None, None, None, None, None, None, None, None, None, None, None, None]
                item['target'] = [None, None, None, None, None, None, None, None, None, None, None, None, None]

                for plus in data:
                    if plus['Concatenar'] == f"{item_base}{target_year - 2}Inventory{' Turns' if turns else ''}":
                        item['averages'].append(plus['Annualized'])

                    if plus['Concatenar'] == f"{item_base}{target_year - 1}Inventory{' Turns' if turns else ''}":
                        item['last'] = [plus['Jan'], plus['Feb'], plus['Mar'], plus['Apr'], plus['May'], plus['Jun'],
                                        plus['Jul'], plus['Aug'], plus['Sep'], plus['Oct'], plus['Nov'], plus['Dec']]
                        item['averages'].append(plus['Annualized'])

                    if plus['Concatenar'] == f"{item_base}{target_year}Inventory {'Turns ' if turns else ''}Target":
                        item['target'] = [plus['Jan'], plus['Jan'], plus['Feb'], plus['Mar'], plus['Apr'], plus['May'],
                                          plus['Jun'],
                                          plus['Jul'], plus['Aug'], plus['Sep'], plus['Oct'], plus['Nov'], plus['Dec']]

                item['averages'].append(item['Annualized'])
                formatted_data.append(item)
                break

    return formatted_data
