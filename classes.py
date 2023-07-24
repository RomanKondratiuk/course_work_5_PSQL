import requests


class DBManager():
    def get_companies_and_vacancies_count(self):
        """ функция которая получает список всех компаний и
            количество вакансий у каждой компании."""
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

        def get_employers_data(company_names):
            """Функция получения данных о работодателях"""

            employers_url = 'https://api.hh.ru/employers'
            params = {
                'text': company_names,
                'per_page': 1  # Получение только одного работодателя
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
            """Функция получения данных о вакансиях работодателей"""

            vacancies_url = 'https://api.hh.ru/vacancies'#?emploier_id=81411435'
            params = {
                'employer_name': employer_name,
                'area': '1',  # Параметр area для Москвы
                'per_page': 50  # Получение только 50 вакансий работодателя
            }
            response = requests.get(vacancies_url, params=params)
            count_all = 0

            if response.status_code == 200:
                vacancies_data = response.json()
                vacancies = vacancies_data['items']
                count = 0
                if vacancies:
                    # print(f"Данные о вакансиях работодателя {employer_name}:")
                    for vacancy in vacancies:
                        count += 1
                        count_all += 1

                        title = vacancy['name']
                        vacancy_url = vacancy['url']

                        # Проверка на значение NONE
                        if vacancy['salary'] is not None:
                            if vacancy['salary']['to'] is not None:
                                salary_max = vacancy['salary']['to']
                            else:
                                salary_max = None
                        else:
                            salary_max = None

                        # Проверка на значение NONE
                        if vacancy['salary'] is not None:
                            if vacancy['salary']['from'] is not None:
                                salary_min = vacancy['salary']['from']
                            else:
                                salary_min = None
                        else:
                            salary_min = None

                        city = vacancy['area']['name']

                        print(title)
                        print(vacancy_url)
                        print(salary_max)
                        print(salary_min)
                        print(city)

                        # print(f" Название - {title}")
                        # print(f" Ссылка на вакансию - {vacancy_url}")
                        # print(f" Максимальная зарплата - {salary_max}")
                        # print(f" Минимальная зарплата - {salary_min}")
                        # print(f" Город - {city}")
                        # print(' ')
                    # print(f"представлено {count} вакансий")


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

    def get_all_vacancies(self):
        """функция которая получает список всех вакансий с указанием названия компании,
           названия вакансии и зарплаты и ссылки на вакансию."""
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
            "Лукойл"
        ]

        all_vacancies = []  # Создаем список для хранения всех вакансий

        def get_employer_vacancies(employer_name):
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
                    count = len(vacancies)
                    all_vacancies.extend(vacancies)  # Добавляем вакансии в общий список
                # print(f"Данные о вакансиях работодателя {employer_name}: {count} вакансий")
            else:
                print(f"Ошибка при выполнении запроса: {response.status_code}")

        # Получение данных для каждой известной компании в России
        for company_name in company_names:
            employer_name = company_name
            if employer_name:
                get_employer_vacancies(employer_name)

        # print(all_vacancies)# Возвращаем список всех вакансий
        for vacancy in all_vacancies:
            title = vacancy['name']
            print(title)

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
            print(f"Ошибка при выполнении запроса: {response.status_code}")

        return None

    # all_vacancies = get_all_vacancies()  # Вызываем функцию и сохраняем результат
    # print(all_vacancies) # Печатаем все вакансии в одном списке

    def get_avg_salary(self):
        """функция которая получает среднюю зарплату по вакансиям."""
        pass

    def get_vacancies_with_higher_salary(self):
        """функция которая получает список всех вакансий, у которых зарплата
            выше средней по всем вакансиям."""
        pass

    def get_vacancies_with_keyword(self):
        """функция которая получает список всех вакансий,
         в названии которых содержатся переданные в метод слова, например “python”."""
        pass
