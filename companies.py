import requests

class YourVacancyManager:
    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        """ Функция которая получает список всех компаний и количество вакансий у каждой компании. """
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

        companies_vacancies_count = {}
        for company_name in company_names:
            employer_name = self.get_employer_data(company_name)
            if employer_name:
                vacancies_count = self.get_vacancies_data(employer_name)
                if vacancies_count is not None:
                    companies_vacancies_count[employer_name] = vacancies_count

        return companies_vacancies_count

    def get_employer_data(self, company_name):
        """ Функция получения данных о работодателе """

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
            print(f"Ошибка при выполнении запроса: {response.status_code}")

        return None

    def get_vacancies_data(self, employer_name):
        """ Функция получения данных о вакансиях работодателей """

        vacancies_url = 'https://api.hh.ru/vacancies'
        params = {
            'employer_name': employer_name,
            'area': '1',  # Параметр area для Москвы
        }
        response = requests.get(vacancies_url, params=params)

        if response.status_code == 200:
            vacancies_data = response.json()
            vacancies_count = vacancies_data['found']
            print(f"Количество вакансий работодателя {employer_name}: {vacancies_count}")
            return vacancies_count
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")

        return None

if __name__ == "__main__":
    vacancy_manager = YourVacancyManager()
    companies_and_vacancies = vacancy_manager.get_companies_and_vacancies_count()
