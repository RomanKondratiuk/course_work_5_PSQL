import requests

# Список известных компаний в России
company_names = [
    "Яндекс",
    "Газпром",
    "Роснефть",
    "Магнит",
    "МТС",
    "Ростелеком",
    "МегаФон",
    "Норникель",
    "Сбербанк",
    "Лукойл",
]

def get_employers_data(company_name):
    """Function for obtaining data about employers"""

    employers_url = 'https://api.hh.ru/employers'
    params = {
        'text': company_name,
        'per_page': 10  # Получение только одного работодателя
    }
    response = requests.get(employers_url, params=params)

    if response.status_code == 200:
        employers_data = response.json()
        if employers_data['found'] > 0:
            employer_name = employers_data['items'][0]['name']
            return employer_name
        else:
            print(f"Не удалось найти информацию о работодателе: {company_name}")
    else:
        print(f"Ошибка при выполнении  запроса: {response.status_code}")

    return None



def get_vacancies_data(employer_name):
    """Function for getting data about employer vacancies"""

    vacancies_url = 'https://api.hh.ru/vacancies'
    params = {
        'employer_name': employer_name,
        'area': '1',  # Параметр area для Москвы
        'per_page': 100  # Получение только 100 вакансий работодателя
    }
    response = requests.get(vacancies_url, params=params)
    if response.status_code == 200:
        vacancies_data = response.json()
        vacancies = vacancies_data['items']
        count = 0
        if vacancies:
            print(f"Данные о вакансиях работодателя {employer_name}:")
            for vacancy in vacancies:
                count += 1
                print(vacancy)

            # title = vacancy['name']
            # print(f" - {title}")
        else:
            print(f"Нет доступных вакансий для работодателя {employer_name}")
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")


# Получение данных для каждой известной компании в России
for company_name in company_names:
    employer_name = get_employers_data(company_name)
    if employer_name:
        get_vacancies_data(employer_name)
        print('===============')


