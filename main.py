from config import config
from data_base import create_database
from classes import DBManager

db_manager = DBManager()


def main():
    all_vacancies = db_manager.get_all_vacancies()
    print(all_vacancies)

    # params = config()
    # create_database('vacancies_hh', params)


if __name__ == '__main__':
    main()
