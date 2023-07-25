from src.hh_api import HeadHunter
from src.jsonclass import JSONFile
from src.sj_api import SuperJob


def main():
    """ Создание экземпляра класса для работы с API сайтов с вакансиями"""
    keyword = "Python"
    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    vacancies_json = []
    vacancies = []

    # Получение вакансий с разных платформ
    for api in (hh, sj):
        vacancies_json.extend(api.get_vacancies(2))

    # запись в файл
    js = JSONFile()
    js.save_vacancies(vacancies_json)

    while 1 == 1:
        user_input = input(
            "1 - Вывести список вакансий\n"
            "2 - Вывести отсортированный список вакансий\n"
            "3 - Вывести список вакансий с мин. зарплатой не меньше указанной\n"
            "0 - Выход\n"
        )
        if user_input == "0":
            break
        elif user_input == "1":
            vacancies = js.read_vacancies()
        elif user_input == "2":
            vacancies = js.sort_by_salary()
        elif user_input == "3":
            min_salary = input("Введите мин. зарплату: ")
            vacancies = js.get_by_salary(min_salary)

        for vacancy in vacancies:
            print(vacancy, end="\n")


if __name__ == "__main__":
    main()
