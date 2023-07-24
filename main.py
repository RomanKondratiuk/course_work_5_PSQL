from config import config
from data_base import create_database, insert_to_tables
from classes import DBManager

db_manager = DBManager()


def main():
    vacancy_data = [
        ("Менеджер по работе с клиентами",
         "https://api.hh.ru/vacancies/81411435?host=hh.ru",
         "250000",
         "80000",
         "Москва"
         ),
        ("Вечерний сотрудник склада от 4х часов, рядом с домом",
         "https://api.hh.ru/vacancies/83450755?host=hh.ru",
         "94000",
         "None",
         "Москва"
         ),
        ("Проводник пассажирского вагона",
         "https://api.hh.ru/vacancies/82982530?host=hh.ru",
         "95000",
         "95000",
         "Москва"
         ),
        ("Промоутер-консультант товаров для красоты и здоровья",
         "https://api.hh.ru/vacancies/82861476?host=hh.ru",
         "60000",
         "42000",
         "Москва"
         ),
        ("Личный водитель",
         "https://api.hh.ru/vacancies/83830410?host=hh.ru",
         "None",
         "100000",
         "Москва"
         ),
        ("Диктор для YouTube канала (Актер озвучки)",
         "https://api.hh.ru/vacancies/82439758?host=hh.ru",
         "70000",
         "50000",
         "Москва"
         ),
        ("Системный аналитик",
         "https://api.hh.ru/vacancies/83830444?host=hh.ru",
         "None",
         "None",
         "Москва"
         ),
        ("Фотограф / фотокорреспондент",
         "https://api.hh.ru/vacancies/83115804?host=hh.ru",
         "200000",
         "100000",
         "Москва"
         )
    ]

    # companies_and_vacancies = db_manager.get_companies_and_vacancies_count()
    # print(companies_and_vacancies)

    # all_vacancies = db_manager.get_all_vacancies()
    # print(all_vacancies)

    # params = config()
    insert_to_tables(vacancy_data)

    # create_database('vacancies_from_hh', params)
    #

if __name__ == '__main__':
    main()
