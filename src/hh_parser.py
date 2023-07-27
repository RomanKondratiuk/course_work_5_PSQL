import requests
from src.constants import TABLE_OF_EMPLOYERS


def get_headhunter_vacancies_by_employer(employer_id, per_page=50):
    """ поиск по id работодателя"""

    api_url = 'https://api.hh.ru/vacancies'
    params = {
        'employer_id': employer_id,
        'per_page': per_page
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        vacancies_data = response.json()
        vacancies = vacancies_data['items']
        all_vacancies = []
        if vacancies:
            print(f"Найдено {len(vacancies)} вакансий от работодателя с id {employer_id}:")
            for vacancy in vacancies:
                if not vacancy["salary"]:
                    salary_max = None
                    salary_min = None
                else:
                    salary_max = vacancy["salary"]["to"]
                    salary_min = vacancy["salary"]["from"]
                all_vacancies.append({
                     "title": vacancy["name"],
                    "url": vacancy["alternate_url"],
                    "salary_max": salary_max,
                    "salary_min": salary_min,
                    "city": vacancy["area"]["name"],
                    "company_id": employer_id
                })
        else:
            print(f"Нет доступных вакансий от работодателя с id {employer_id}")
        return all_vacancies
    else:
        print(
            f"Не удалось получить информацию о вакансиях от работодателя с id {employer_id}, статус код: {response.status_code}")


if __name__ == "__main__":
    employer_id = '78638'  # идентификатор работодателя


def get_all_vacancies():
    """Функция для заполнения списка необходимыми данными о вакансиях"""
    all_vacancies = []

    for company in TABLE_OF_EMPLOYERS:
        all_vacancies.extend(get_headhunter_vacancies_by_employer(company['id']))
    return all_vacancies
