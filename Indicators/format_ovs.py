import datetime

target_year = int((datetime.date.today() - datetime.timedelta(days=datetime.date.today().day)).strftime("%Y"))

def delete_months(item):
    del item[f'Acum {target_year - 2}']
    del item[f'Acum {target_year - 1}']
    del item[f'Acum {target_year}']
    del item['JAN']
    del item['FEV']
    del item['MAR']
    del item['ABR']
    del item['MAI']
    del item['JUN']
    del item['JUL']
    del item['AGO']
    del item['SET']
    del item['OUT']
    del item['NOV']
    del item['DEZ']

def formatar_json(data):
    formatted_data = []
    for item in data:
        if item['Indicador']:
            if '%' in item['Indicador'] and 'razo' in item['Indicador']:
                item['averages'] = [item[f'Acum {target_year-2}'], item[f'Acum {target_year-1}'],
                                    item[f'Acum {target_year}']]
                item['data'] = [item['JAN'], item['FEV'], item['MAR'], item['ABR'], item['MAI'], item['JUN'],
                                item['JUL'], item['AGO'], item['SET'], item['OUT'], item['NOV'], item['DEZ']]
                delete_months(item)
                formatted_data.append(item)

    return formatted_data
