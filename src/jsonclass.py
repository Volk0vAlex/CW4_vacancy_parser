from src.abstract import JSONABS
import json
from src.vacancy import Vacancy


class JSONFile(JSONABS):

    def save_vacancies(self, vacancies_list):
        with open("vacancies.json", "w", encoding="utf-8") as jf:
            json.dump(vacancies_list, jf, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        with open("vacancies.json", "r", encoding="utf-8") as jf:
            vacancies_list = []
            vacancies_json = json.load(jf)

            for i in vacancies_json:
                vacancies_list.append(Vacancy(i["id"], i["job_name"],
                                              i["job_url"], i["salary_from"], i["salary_to"], i["salary_str"],
                                              i["requirement"], i["responsibility"], i["location"], i["firm"]))

            return vacancies_list

    def sort_by_salary(self):
        """Получение отсортированного списка"""
        vacancies_list = self.read_vacancies()
        vacancies_list = sorted(vacancies_list, reverse=True)
        return vacancies_list

    def get_by_salary(self, min_salary):
        """Получение списка по мин. з/п"""
        min_salary = int(min_salary)
        vacancies = []
        if min_salary < 0 or not isinstance(min_salary, int):
            print("Неверное значение мин. з/п!")
        else:
            vacancies_list = self.read_vacancies()
            for i in vacancies_list:
                if i.salary_from is not None and i.salary_from >= min_salary:
                    vacancies.append(i)

            vacancies = sorted(vacancies, reverse=True)
        return vacancies
