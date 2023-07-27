import psycopg2


class DBManager():
    def __init__(self, db_name, params):
        self.conn = psycopg2.connect(dbname=db_name, **params)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """ функция которая получает список всех компаний и
            количество вакансий у каждой компании."""

        self.cur.execute(""" SELECT companies.title, COUNT(*) AS count_vacancies from companies
                             JOIN vacancies on companies.company_id = vacancies.company_id
                             GROUP BY companies.title""")
        return self.cur.fetchall()

    def get_all_vacancies(self):
        """функция которая получает список всех вакансий с указанием названия компании,
           названия вакансии и зарплаты и ссылки на вакансию."""

        self.cur.execute(""" SELECT companies.title, vacancies.title, vacancies.vacancy_url, vacancies.salary_min, vacancies.salary_max
                             FROM vacancies 
                             JOIN companies ON vacancies.company_id = companies.company_id;
                        """)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """функция которая получает среднюю зарплату по вакансиям."""
        self.cur.execute(""" select ROUND(avg(salary_max)) as avg_salary from vacancies
                            where salary_max is not null 
                              """)
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """функция которая получает список всех вакансий, у которых зарплата
            выше средней по всем вакансиям."""
        self.cur.execute("""SELECT companies.title, vacancies.title, vacancies.vacancy_url, vacancies.salary_min, vacancies.salary_max
                            FROM vacancies 
                            JOIN companies ON vacancies.company_id = companies.company_id
                            WHERE vacancies.salary_max > (SELECT ROUND(AVG(salary_max)) AS avg_salary FROM vacancies WHERE salary_max IS NOT NULL);
                        """)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self):
        """функция которая получает список всех вакансий,
         в названии которых содержатся переданные в метод слова, например “python”."""

        self.cur.execute("""select * from vacancies
                            where title like '%Python%'""")
        return self.cur.fetchall()

    def disconnect(self):
        """ Функция для отключения от базы данных"""
        self.conn.close()
