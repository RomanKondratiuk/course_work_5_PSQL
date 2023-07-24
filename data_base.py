import json

import psycopg2


def create_database(database_name: str, params: dict):
    """ Создание базы данных для сохранения данных """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    # cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    # connection to database
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE companies (
                        channel_id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL
                          )
                    """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                title VARCHAR NOT NULL,
                vacancy_url TEXT,
                salary_max varchar,
                salary_min varchar,
                city VARCHAR(50)
            )
        """)

    conn.commit()
    conn.close()


def insert_to_tables(vacancy_data):
    """Скрипт для заполнения данными таблиц в БД Postgres."""
    conn = psycopg2.connect('''
        dbname=vacancies_from_hh
        user=postgres
        password=20010906
        host=localhost
        port=5432''')

    c = conn.cursor
    # Вставка данных из списка vacancies_list
    c.execute('INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s )', vacancy_data)

    conn.commit()  # Сохранение изменений
    conn.close()  # Закрытие соединения с базой данных



