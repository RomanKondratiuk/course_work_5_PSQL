# сделай с этой мне список вакансий с  кортежами по 5 элементов и выдай это кодом
import requests

vacancies = [
    ("Менеджер по работе с клиентами", "https://api.hh.ru/vacancies/81411435?host=hh.ru", 250000, 80000, "Москва"),
    ("Диктор", "https://api.hh.ru/vacancies/82868729?host=hh.ru", None, None, "Москва"),
    ("Проводник пассажирского вагона", "https://api.hh.ru/vacancies/82982530?host=hh.ru", 95000, 95000, "Москва"),
    ("Персональный водитель", "https://api.hh.ru/vacancies/83933684?host=hh.ru", 100000, None, "Москва"),
    ("Семейный водитель для женщины (КП Монтевиль)", "https://api.hh.ru/vacancies/83940673?host=hh.ru", 100000, 100000, "Москва"),
    ("Менеджер чатов на дому (в Яндекс)", "https://api.hh.ru/vacancies/83194123?host=hh.ru", 40000, 26000, "Москва"),
    ("Бухгалтер", "https://api.hh.ru/vacancies/83967733?host=hh.ru", 150000, 145000, "Москва"),
    ("Диктор для YouTube канала (Актер озвучки)", "https://api.hh.ru/vacancies/82439758?host=hh.ru", 70000, 50000, "Москва"),
    ("Личный водитель", "https://api.hh.ru/vacancies/83957068?host=hh.ru", None, None, "Москва"),
    ("Помощник редактора", "https://api.hh.ru/vacancies/83246274?host=hh.ru", 30000, None, "Москва"),
    ("Менеджер по продажам", "https://api.hh.ru/vacancies/83402718?host=hh.ru", 250000, 150000, "Москва"),
    ("Учитель физической культуры", "https://api.hh.ru/vacancies/83145998?host=hh.ru", None, 85000, "Москва"),
    ("Охранник", "https://api.hh.ru/vacancies/83177277?host=hh.ru", None, 270000, "Москва"),
    ("Психолог", "https://api.hh.ru/vacancies/83960978?host=hh.ru", 65000, 60000, "Москва"),
    ("Персональный водитель к руководителю", "https://api.hh.ru/vacancies/83941840?host=hh.ru", 150000, None, "Москва"),
    ("Заместитель генерального директора (СОО)", "https://api.hh.ru/vacancies/83968165?host=hh.ru", None, None, "Москва"),
    ("Помощник дизайнера интерьера", "https://api.hh.ru/vacancies/83176125?host=hh.ru", 30000, 15000, "Москва"),
    ("Помощник бухгалтера/ассистент/бухгалтер, удаленно", "https://api.hh.ru/vacancies/82765466?host=hh.ru", 40000, 20000, "Москва"),
    ("Охранник-администратор в офис класса \"А+\"", "https://api.hh.ru/vacancies/80665071?host=hh.ru", 102000, 86000, "Москва"),
    ("Руководитель проектов", "https://api.hh.ru/vacancies/83951044?host=hh.ru", None, 400000, "Москва"),
    ("Медсестра/медицинский брат", "https://api.hh.ru/vacancies/83098369?host=hh.ru", 270000, 200000, "Москва"),
    ("Секретарь/личный помощник руководителя", "https://api.hh.ru/vacancies/83927611?host=hh.ru", None, 150000, "Москва"),
    ("Водитель в аптеку", "https://api.hh.ru/vacancies/83944895?host=hh.ru", None, 90000, "Москва"),
    ("Персональный водитель", "https://api.hh.ru/vacancies/83967227?host=hh.ru", 80000, None, "Москва"),
    ("Учитель английского языка", "https://api.hh.ru/vacancies/82438130?host=hh.ru", None, 80000, "Москва"),
    ("Специалист учебного отдела факультета", "https://api.hh.ru/vacancies/82869216?host=hh.ru", None, 45000, "Москва"),
    ("Водитель (Мариуполь/Луганск)", "https://api.hh.ru/vacancies/83947336?host=hh.ru", 100000, 100000, "Москва"),
    ("Специалист в отдел мультимедийных технологий", "https://api.hh.ru/vacancies/82682288?host=hh.ru", 75600, 53300, "Москва"),
    ("Сотрудник службы безопасности", "https://api.hh.ru/vacancies/82300596?host=hh.ru", 175000, None, "Москва"),
    ("Кассир в кассу организации", "https://api.hh.ru/vacancies/83943296?host=hh.ru", 70000, 50000, "Москва"),
    ("Программист-стажер (удаленно)", "https://api.hh.ru/vacancies/83935515?host=hh.ru", 17000, 17000, "Москва"),
    ("Сотрудник ГБР", "https://api.hh.ru/vacancies/83946519?host=hh.ru", 160000, 140000, "Москва"),
    ("Персональный водитель для руководителя", "https://api.hh.ru/vacancies/83969349?host=hh.ru", 100000, 100000, "Москва"),
    ("Менеджер по продажам (АС Проект)", "https://api.hh.ru/vacancies/83376562?host=hh.ru", None, 100000, "Москва"),
    ("Заместитель главного бухгалтера", "https://api.hh.ru/vacancies/83959701?host=hh.ru", None, 200000, "Москва"),
    ("Специалист отдела кадрового администрирования", "https://api.hh.ru/vacancies/83952287?host=hh.ru", 120000, 100000, "Москва"),
    ("Специалист технической поддержки (2 уровня)", "https://api.hh.ru/vacancies/83921424?host=hh.ru", 120000, 120000, "Москва"),
    ("Помощник по хозяйству-водитель", "https://api.hh.ru/vacancies/83950246?host=hh.ru", 120000, 100000, "Москва"),
    ("Офис-менеджер", "https://api.hh.ru/vacancies/83939755?host=hh.ru", None, None, "Москва"),
    ("Повар VIP в семью", "https://api.hh.ru/vacancies/83954881?host=hh.ru", 250000, 250000, "Москва"),
    ("IOS-разработчик (стажер/trainee)", "https://api.hh.ru/vacancies/83962652?host=hh.ru", None, None, "Москва"),
    ("Офицер фельдсвязи", "https://api.hh.ru/vacancies/71033357?host=hh.ru", None, 54000, "Москва"),
    ("Финансовый аналитик/ Финансовый контролер", "https://api.hh.ru/vacancies/83963585?host=hh.ru", None, 200000, "Москва"),
    ("Помощник депутата Государственной Думы", "https://api.hh.ru/vacancies/83732310?host=hh.ru", 150000, 100000, "Москва"),
    ("Охранник в офис", "https://api.hh.ru/vacancies/83960483?host=hh.ru", None, 52000, "Москва"),
    ("Личный помощник Эксперту, Блогеру (Онлайн/ Оффлайн)", "https://api.hh.ru/vacancies/82806950?host=hh.ru", None, 50000, "Москва"),
    ("Главный бухгалтер", "https://api.hh.ru/vacancies/83922976?host=hh.ru", 280000, 220000, "Москва"),
    ("Медицинская сестра/медицинский брат процедурной", "https://api.hh.ru/vacancies/82367208?host=hh.ru", None, 75000, "Москва"),
    ("Помощник продюсера", "https://api.hh.ru/vacancies/83900911?host=hh.ru", None, 80000, "Москва"),
    ("Персональный водитель / Семейный водитель", "https://api.hh.ru/vacancies/83931847?host=hh.ru", None, 85000, "Москва"),
]


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

        vacancies_url = 'https://api.hh.ru/vacancies'  # ?emploier_id=81411435'
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

                    print(title, vacancy_url, salary_max, salary_min, city)
                    # print(vacancy_url)
                    # print(salary_max)
                    # print(salary_min)
                    # print(city)

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

get_companies_and_vacancies_count(vacancies)