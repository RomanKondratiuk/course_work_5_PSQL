from src.config import config
from src.constants import DB_NAME
from src.data_base import create_database, insert_to_tables
from src.db_manager import DBManager
import re
from decimal import Decimal


def main():
    params = config()

    print("Создаем базу данных и таблицы...")
    create_database(DB_NAME, params)
    print("База данных и таблицы созданы!")
    print("Добавляем данные в базу данных...")
    insert_to_tables(DB_NAME, params)
    print("Данные успешно внесены в базу данных!")
    print("")

    db_manager = DBManager(DB_NAME, params)
    user_input = input("""Для получения списка всех компаний и количества вакансий у каждой компании нажите 1: """)

    if user_input == '1':
        for elem in db_manager.get_companies_and_vacancies_count():
            print("Название компании:", elem[0])
            print("Кол-во вакансий:", elem[1])
            print("=" * 30)
    else:
        raise PermissionError("Вы решили отказаться...")

    user_input = input("Для вывода всех вакансий с более детальной инфориацией нажмите 2: ")
    if user_input == '2':
        for elem in db_manager.get_all_vacancies():
            print('Название компании:', elem[0])
            print('Название вакансии:', elem[1])
            print('Ссылка на вакансию:', elem[2])
            print('Минимальная зарплата:', elem[3])
            print('Максимальная зарплата:', elem[4])
            print("=" * 30)
    else:
        raise PermissionError("Вы решили отказаться...")

    user_input = input("Для вывода средней зарплаты нажмите 3: ")
    if user_input == '3':
        avg = db_manager.get_avg_salary()
        print(avg)
        print("=" * 30)
    else:
        raise PermissionError("Вы решили отказаться...")

    user_input = input("""Для вывода списка всех вакансий, у которых зарплата  выше средней по всем вакансиям нажмите 4: """)

    if user_input == '4':
        for elem in db_manager.get_vacancies_with_higher_salary():
            print('Название компании:', elem[0])
            print('Название вакансии:', elem[1])
            print('Ссылка на вакансию:', elem[2])
            print('Минимальная зарплата:', elem[3])
            print('Максимальная зарплата:', elem[4])
            print("=" * 30)
    else:
        raise PermissionError("Вы решили отказаться...")

    user_input = input(""" Для вывода списка всех вакансий,  в названии которых содержатся переданные в метод слова, например “python” нажмите 5: """)
    if user_input == '5':
        for elem in db_manager.get_vacancies_with_keyword():
            print('Название компании:', elem[0])
            print('Название вакансии:', elem[1])
            print('Ссылка на вакансию:', elem[2])
            print('Минимальная зарплата:', elem[3])
            print('Максимальная зарплата:', elem[4])
            print("=" * 30)
    else:
        raise PermissionError("Вы решили отказаться...")

    db_manager.disconnect()


if __name__ == '__main__':
    main()
