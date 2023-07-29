from src.config import config
from src.constants import DB_NAME
from src.data_base import create_database, insert_to_tables
from src.db_manager import DBManager

# params = config()
# db_manager = DBManager(DB_NAME, params)


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


    def get_user_input():
        for i in range(5):

            print("Вам представлены следуюшие варианты реализации программы:")

            print("1. Для получения списка всех компаний и количества вакансий у каждой компании нажмите 1")
            print("=" * 50)
            print("2. Для вывода всех вакансий с более детальной информацией нажмите 2")
            print("=" * 50)
            print("3. Для вывода средней зарплаты нажмите 3")
            print("=" * 50)
            print("4. Для вывода списка всех вакансий, у которых зарплата  выше средней по всем вакансиям нажмите 4")
            print("=" * 50)
            print(
                "5. Для вывода списка всех вакансий,  в названии которых содержатся переданные в метод слова, например “python” нажмите 5")
            print("=" * 50)

            user_input = input("Введите ваш выбор: ")

            if user_input == '1':
                for elem in db_manager.get_companies_and_vacancies_count():
                    print("Название компании:", elem[0])
                    print("Кол-во вакансий:", elem[1])
                    print("=" * 30)

            elif user_input == '2':
                for elem in db_manager.get_all_vacancies():
                    print('Название компании:', elem[0])
                    print('Название вакансии:', elem[1])
                    print('Ссылка на вакансию:', elem[2])
                    print('Минимальная зарплата:', elem[3])
                    print('Максимальная зарплата:', elem[4])
                    print("=" * 30)

            elif user_input == '3':
                avg_salary = db_manager.get_avg_salary()
                # Извлекаем первый элемент списка по индексу 0
                first_result = avg_salary[0]
                # Извлекаем значение Decimal из кортежа
                decimal_value = first_result[0]
                # Преобразуем значение Decimal в строку
                avg_string = str(decimal_value)
                print(f"Cредняя зарплата: {avg_string}")
                print("=" * 30)

            elif user_input == '4':
                for elem in db_manager.get_vacancies_with_higher_salary():
                    print('Название компании:', elem[0])
                    print('Название вакансии:', elem[1])
                    print('Ссылка на вакансию:', elem[2])
                    print('Минимальная зарплата:', elem[3])
                    print('Максимальная зарплата:', elem[4])
                    print("=" * 30)

            elif user_input == '5':
                user_input = input('Введите ключевое слово по которому будет осуществляться поиск: ')
                key_word = user_input.lower()
                count_vacancies = 0

                for elem in db_manager.get_vacancies_with_keyword(key_word):
                    print('Название вакансии:', elem[1])
                    print('Ссылка на вакансию:', elem[2])
                    print('Минимальная зарплата:', elem[3])
                    print('Максимальная зарплата:', elem[4])
                    print("=" * 30)
                    count_vacancies += 1
                print(f"Найдено {count_vacancies} вакансий по ключевому слову '{key_word}'!")
            else:
                print("Некорректный ввод, пожалуйста, попробуйте снова.")

        raise PermissionError("Превышено количество попыток ввода.")

    try:
        get_user_input()
    except PermissionError as e:
        print(e)

    finally:
        db_manager.disconnect()


if __name__ == '__main__':
    main()
