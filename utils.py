# import requests
#
# # Список известных компаний в России
# company_names = [
#     "Яндекс",
#     "Газпром",
#     "Роснефть",
#     "Магнит",
#     "МТС",
#     "Ростелеком",
#     "МегаФон",
#     "Норникель",
#     "Сбербанк",
#     "Лукойл",
# ]
#
# def get_employers_data(company_names):
#     employers_data = []
#
#     employers_url = 'https://api.hh.ru/employers'
#     for company_name in company_names:
#         params = {'text': company_name, 'per_page': 1}
#         response = requests.get(employers_url, params=params)
#
#         if response.status_code == 200:
#             data = response.json()
#             if data['found'] > 0:
#                 employer_id = data['items'][0]['id']
#                 employers_data.append({'name': company_name, 'id': employer_id})
#             else:
#                 print(f"Не удалось найти информацию о работодателе: {company_name}")
#         else:
#             print(f"Ошибка при выполнении запроса: {response.status_code}")
#
#     return employers_data
#
# def get_all_vacancies(employer_id):
#     all_vacancies = []
#
#     vacancies_url = 'https://api.hh.ru/vacancies'
#     page = 0
#     per_page = 100
#
#     while True:
#         params = {'employer_id': employer_id, 'per_page': per_page, 'page': page}
#         response = requests.get(vacancies_url, params=params)
#
#         if response.status_code == 200:
#             data = response.json()
#             vacancies = data['items']
#             if not vacancies:
#                 break
#
#             all_vacancies.extend(vacancies)
#             if len(vacancies) < per_page:
#                 break  # Reached the end of vacancies
#
#             page += 1
#         else:
#             print(f"Ошибка при выполнении запроса: {response.status_code}")
#             break
#
#     return all_vacancies
#
# # Получение данных о работодателях
# employers_data = get_employers_data(company_names)
#
# # Получение данных о вакансиях для каждого работодателя
# for employer in employers_data:
#     employer_name = employer['name']
#     employer_id = employer['id']
#     vacancies_data = get_all_vacancies(employer_id)
#
#     print(employer_name)
#     print(len(vacancies_data))
#
# #
# #     if vacancies_data:
# #         print(f"Данные о вакансиях работодателя {employer_name}:")
# #         for vacancy in vacancies_data:
# #             title = vacancy['name']
# #             print(f" - {title}")
# #         print(f"Всего {len(vacancies_data)} вакансий")
# #     else:
# #         print(f"Нет доступных вакансий для работодателя {employer_name}")
# #
# #     print('===============')
