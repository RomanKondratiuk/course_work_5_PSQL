import requests

def get_companies_and_vacancies_count():
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

    def get_employer_data(company_name):
        employers_url = 'https://api.hh.ru/employers'
        params = {
            'text': company_name,
            'per_page': 1
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
            print(f"Ошибка при выполнении запроса: {response.status_code}")

        return None

    def get_vacancies_data(employer_name):
        vacancies_url = 'https://api.hh.ru/vacancies'
        per_page = 50
        count_all = 0

        params = {
            'employer_name': employer_name,
            'area': '1',
            'per_page': per_page
        }

        while True:
            response = requests.get(vacancies_url, params=params)

            if response.status_code == 200:
                vacancies_data = response.json()
                vacancies = vacancies_data['items']
                count = len(vacancies)
                if vacancies:
                    for vacancy in vacancies:
                        count_all += 1
                        title = vacancy['name']
                        vacancy_url = vacancy['url']
                        salary = vacancy.get('salary')
                        salary_max = salary.get('to', 'Не указано') if salary else 'Не указано'
                        salary_min = salary.get('from', 'Не указано') if salary else 'Не указано'
                        city = vacancy['area']['name']

                        print(f"{employer_name}, {title}, {vacancy_url}, {salary_max}, {salary_min}, {city}")

                        if count_all == per_page:
                            break

                    if count_all == per_page:
                        break

                    if count < per_page:
                        break
                    params['page'] = vacancies_data['page'] + 1
                else:
                    print(f"Нет доступных вакансий для работодателя {employer_name}")
                    break
            else:
                print(f"Ошибка при выполнении запроса: {response.status_code}")
                break

        # print(f"Представлено {count_all} вакансий для работодателя {employer_name}")
        # print('=' * 30)

    for company_name in company_names:
        employer_name = get_employer_data(company_name)
        if employer_name:
            get_vacancies_data(employer_name)


if __name__ == "__main__":
    get_companies_and_vacancies_count()
