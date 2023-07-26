import requests


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
        if vacancies:
            print(f"Найдено {len(vacancies)} вакансий от работодателя с id {employer_id}:")
            for vacancy in vacancies:
                print(f"Название: {vacancy['name']}")
                if vacancy.get('salary'):
                    print(f"Зарплата: {vacancy['salary'].get('from', 'Не указано')} - {vacancy['salary'].get('to', 'Не указано')} {vacancy['salary'].get('currency', 'Не указана')}")
                else:
                    print("Зарплата: Не указано")
                print(f"Город: {vacancy['area']['name']}")
                print(f"Описание: {vacancy['description']}")
                print(f"Ссылка: {vacancy['alternate_url']}")
                print("="*30)
        else:
            print(f"Нет доступных вакансий от работодателя с id {employer_id}")
    else:
        print(f"Не удалось получить информацию о вакансиях от работодателя с id {employer_id}, статус код: {response.status_code}")


if __name__ == "__main__":
    employer_id = '78638'  # Замените на реальный идентификатор работодателя
    get_headhunter_vacancies_by_employer(employer_id)
