from config import config
from data_base import create_database, insert_to_tables
from classes import DBManager

db_manager = DBManager()


def main():
    vacancy_data = [
        ("Менеджер по работе с клиентами", "https://api.hh.ru/vacancies/81411435?host=hh.ru", 250000, 80000, "Москва"),
        ("Диктор", "https://api.hh.ru/vacancies/82868729?host=hh.ru", None, None, "Москва"),
        ("Проводник пассажирского вагона", "https://api.hh.ru/vacancies/82982530?host=hh.ru", 95000, 95000, "Москва"),
        ("Персональный водитель", "https://api.hh.ru/vacancies/83933684?host=hh.ru", 100000, None, "Москва"),
        ("Семейный водитель для женщины (КП Монтевиль)", "https://api.hh.ru/vacancies/83940673?host=hh.ru", 100000,
         100000, "Москва"),
        (
        "Менеджер чатов на дому (в Яндекс)", "https://api.hh.ru/vacancies/83194123?host=hh.ru", 40000, 26000, "Москва"),
        ("Бухгалтер", "https://api.hh.ru/vacancies/83967733?host=hh.ru", 150000, 145000, "Москва"),
        ("Диктор для YouTube канала (Актер озвучки)", "https://api.hh.ru/vacancies/82439758?host=hh.ru", 70000, 50000,
         "Москва"),
        ("Личный водитель", "https://api.hh.ru/vacancies/83957068?host=hh.ru", None, None, "Москва"),
        ("Помощник редактора", "https://api.hh.ru/vacancies/83246274?host=hh.ru", 30000, None, "Москва"),
        ("Менеджер по продажам", "https://api.hh.ru/vacancies/83402718?host=hh.ru", 250000, 150000, "Москва"),
        ("Учитель физической культуры", "https://api.hh.ru/vacancies/83145998?host=hh.ru", None, 85000, "Москва"),
        ("Охранник", "https://api.hh.ru/vacancies/83177277?host=hh.ru", None, 270000, "Москва"),
        ("Психолог", "https://api.hh.ru/vacancies/83960978?host=hh.ru", 65000, 60000, "Москва"),
        ("Персональный водитель к руководителю", "https://api.hh.ru/vacancies/83941840?host=hh.ru", 150000, None,
         "Москва"),
        ("Заместитель генерального директора (СОО)", "https://api.hh.ru/vacancies/83968165?host=hh.ru", None, None,
         "Москва"),
        ("Помощник дизайнера интерьера", "https://api.hh.ru/vacancies/83176125?host=hh.ru", 30000, 15000, "Москва"),
        ("Помощник бухгалтера/ассистент/бухгалтер, удаленно", "https://api.hh.ru/vacancies/82765466?host=hh.ru", 40000,
         20000, "Москва"),
        (
        "Охранник-администратор в офис класса \"А+\"", "https://api.hh.ru/vacancies/80665071?host=hh.ru", 102000, 86000,
        "Москва"),
        ("Руководитель проектов", "https://api.hh.ru/vacancies/83951044?host=hh.ru", None, 400000, "Москва"),
        ("Медсестра/медицинский брат", "https://api.hh.ru/vacancies/83098369?host=hh.ru", 270000, 200000, "Москва"),
        ("Секретарь/личный помощник руководителя", "https://api.hh.ru/vacancies/83927611?host=hh.ru", None, 150000,
         "Москва"),
        ("Водитель в аптеку", "https://api.hh.ru/vacancies/83944895?host=hh.ru", None, 90000, "Москва"),
        ("Персональный водитель", "https://api.hh.ru/vacancies/83967227?host=hh.ru", 80000, None, "Москва"),
        ("Учитель английского языка", "https://api.hh.ru/vacancies/82438130?host=hh.ru", None, 80000, "Москва"),
        ("Специалист учебного отдела факультета", "https://api.hh.ru/vacancies/82869216?host=hh.ru", None, 45000,
         "Москва"),
        ("Водитель (Мариуполь/Луганск)", "https://api.hh.ru/vacancies/83947336?host=hh.ru", 100000, 100000, "Москва"),
        (
        "Специалист в отдел мультимедийных технологий", "https://api.hh.ru/vacancies/82682288?host=hh.ru", 75600, 53300,
        "Москва"),
        ("Сотрудник службы безопасности", "https://api.hh.ru/vacancies/82300596?host=hh.ru", 175000, None, "Москва"),
        ("Кассир в кассу организации", "https://api.hh.ru/vacancies/83943296?host=hh.ru", 70000, 50000, "Москва"),
        ("Программист-стажер (удаленно)", "https://api.hh.ru/vacancies/83935515?host=hh.ru", 17000, 17000, "Москва"),
        ("Сотрудник ГБР", "https://api.hh.ru/vacancies/83946519?host=hh.ru", 160000, 140000, "Москва"),
        ("Персональный водитель для руководителя", "https://api.hh.ru/vacancies/83969349?host=hh.ru", 100000, 100000,
         "Москва"),
        ("Менеджер по продажам (АС Проект)", "https://api.hh.ru/vacancies/83376562?host=hh.ru", None, 100000, "Москва"),
        ("Заместитель главного бухгалтера", "https://api.hh.ru/vacancies/83959701?host=hh.ru", None, 200000, "Москва"),
        ("Специалист отдела кадрового администрирования", "https://api.hh.ru/vacancies/83952287?host=hh.ru", 120000,
         100000, "Москва"),
        ("Специалист технической поддержки (2 уровня)", "https://api.hh.ru/vacancies/83921424?host=hh.ru", 120000,
         120000, "Москва"),
        ("Помощник по хозяйству-водитель", "https://api.hh.ru/vacancies/83950246?host=hh.ru", 120000, 100000, "Москва"),
        ("Офис-менеджер", "https://api.hh.ru/vacancies/83939755?host=hh.ru", None, None, "Москва"),
        ("Повар VIP в семью", "https://api.hh.ru/vacancies/83954881?host=hh.ru", 250000, 250000, "Москва"),
        ("IOS-разработчик (стажер/trainee)", "https://api.hh.ru/vacancies/83962652?host=hh.ru", None, None, "Москва"),
        ("Офицер фельдсвязи", "https://api.hh.ru/vacancies/71033357?host=hh.ru", None, 54000, "Москва"),
        ("Финансовый аналитик/ Финансовый контролер", "https://api.hh.ru/vacancies/83963585?host=hh.ru", None, 200000,
         "Москва"),
        ("Помощник депутата Государственной Думы", "https://api.hh.ru/vacancies/83732310?host=hh.ru", 150000, 100000,
         "Москва"),
        ("Охранник в офис", "https://api.hh.ru/vacancies/83960483?host=hh.ru", None, 52000, "Москва"),
        ("Личный помощник Эксперту, Блогеру (Онлайн/ Оффлайн)", "https://api.hh.ru/vacancies/82806950?host=hh.ru", None,
         50000, "Москва"),
        ("Главный бухгалтер", "https://api.hh.ru/vacancies/83922976?host=hh.ru", 280000, 220000, "Москва"),
        ("Медицинская сестра/медицинский брат процедурной", "https://api.hh.ru/vacancies/82367208?host=hh.ru", None,
         75000, "Москва"),
        ("Помощник продюсера", "https://api.hh.ru/vacancies/83900911?host=hh.ru", None, 80000, "Москва"),
        ("Персональный водитель / Семейный водитель", "https://api.hh.ru/vacancies/83931847?host=hh.ru", None, 85000,
         "Москва"),
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
