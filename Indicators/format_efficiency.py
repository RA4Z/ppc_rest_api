import datetime

target_year = int((datetime.date.today() - datetime.timedelta(days=datetime.date.today().day)).strftime("%Y"))


def delete_months(item):
    del item[target_year - 2]
    del item[target_year - 1]
    del item[target_year]
    del item['Total']
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
        if item['Empresa'] is not None and item['Field'] is not None:
            formatted_data.append(item)
            item['averages'] = [item[target_year - 2], item[target_year - 1], item[target_year]]
            months = [item['Jan'], item['Feb'], item['Mar'], item['Apr'], item['May'], item['Jun'],
                      item['Jul'], item['Aug'], item['Sep'], item['Oct'], item['Nov'], item['Dec']]
            item['data'] = [x if x != ' ' and x != 0 else None for x in months]
            delete_months(item)

    new_data = []
    for company_data in formatted_data:
        company_name = company_data['Empresa']

        # Verifica se a empresa já está em new_data
        company_exists = any(company['Empresa'] == company_name for company in new_data)

        if not company_exists:
            company_dict = {'Empresa': company_name, 'Indicador': f'{company_name} Efficiency'}
            for field_data in formatted_data:
                if field_data['Empresa'] == company_name and field_data['Field'] is not None:
                    field_name = (field_data['Field'].replace(" ", "_"))
                    if "Hrs_" in field_name:
                        field_name = field_name[:field_name.find("Hrs_") + len("Hrs")]
                    else:
                        field_name = "_".join(field_name.split("_")[:3])

                    company_dict[field_name] = {
                        'averages': field_data['averages'],
                        'data': field_data['data']
                    }
            company_dict['averages'] = company_dict['Total_Efficiency_Registered']['averages']
            company_dict['data'] = company_dict['Total_Efficiency_Registered']['data']
            company_dict['Meta'] = None
            new_data.append(company_dict)

    return new_data
