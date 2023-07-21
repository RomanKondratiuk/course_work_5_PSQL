import psycopg2


def create_database(database_name: str, params: dict):
    """ Создание базы данных для сохранения данных """
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    # connection to database
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        cur.execute("""
                    CREATE TABLE companies (
                        channel_id SERIAL PRIMARY KEY,
                        title VARCHAR(255) NOT NULL,
                        city VARCHAR(255),
                        url TEXT
                          )
                    """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                title VARCHAR NOT NULL,
                requirements TEXT,
                vacancy_url TEXT,
                salary_min varchar,
                salary_min varchar
            )
        """)

    conn.commit()
    conn.close()
