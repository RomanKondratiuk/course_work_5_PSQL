
import psycopg2
from src.constants import TABLE_OF_EMPLOYERS
from src.hh_parser import get_all_vacancies


def create_database(database_name: str, params: dict):
    """ Создание базы данных для сохранения данных """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    # connection to database
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE companies (
                        company_id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL
                          )
                    """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                title VARCHAR NOT NULL,
                vacancy_url TEXT,
                salary_max int,
                salary_min int,
                city VARCHAR(50),
                company_id  INT REFERENCES companies(company_id)
            )
        """)

    conn.commit()
    conn.close()


def insert_to_tables(db_name, params):
    """Скрипт для заполнения данными таблиц в БД Postgres."""
    conn = psycopg2.connect(
        dbname=db_name,
        **params
    )

    c = conn.cursor()
    conn.autocommit = True  # Сохранение изменений

    # Вставка данных из списка vacancies_list
    for company in TABLE_OF_EMPLOYERS:
        c.execute(
            'INSERT INTO companies(company_id, title) VALUES ( %s, %s)',
            (company['id'], company['title']))

    all_vacancies = get_all_vacancies()
    for vacancy in all_vacancies:
        c.execute(
            'INSERT INTO vacancies(title, vacancy_url, salary_max, salary_min, city, company_id) VALUES( %s, %s, %s, %s, %s, %s )',
            (vacancy['title'], vacancy['url'], vacancy['salary_max'], vacancy['salary_min'], vacancy['city'],
             vacancy['company_id']))

    conn.close()  # Закрытие соединения с базой данных
