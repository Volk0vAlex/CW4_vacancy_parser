import os
import requests
from src.abstract import GetVacanciesAbstractClass


class SuperJob(GetVacanciesAbstractClass):
    def __init__(self, keyword):
        self.__header = {"X-Api-App-Id": os.getenv("SJ_API_KEY")}
        self.__params = {
            "keyword": keyword,
            "page": 0,
            "count": 100
        }
        self.__full_vacancies = []
        self.salary_from: int = None
        self.salary_to: int = None
        self.salary_str = ''

    def get_vacancies(self, page_count=1):
        page = self.__params["page"]
        while page < page_count:
            print(f"SuperJob, Страница {page+1}", end=": ")
            vacancies_list = self.get_request()
            print(f"Найдено {len(vacancies_list)}")

            self.__full_vacancies.extend(vacancies_list)
            page += 1
            self.__params["page"] = page

        vacancies_list = self.get_vacancy_info()
        return vacancies_list

    def get_request(self):
        response = requests.get("https://api.superjob.ru/2.0/vacancies", headers=self.__header, params=self.__params)
        # print(json.dumps(response.json(), indent=2, ensure_ascii=False))
        return response.json()["objects"]

    def get_vacancy_info(self):
        vacancies = []
        for item in self.__full_vacancies:
            self.get_salary(item["payment_from"], item["payment_to"], item["currency"])
            vacancies.append({
                "id": item["id"],
                "job_name": item['profession'],
                "job_url":  item['link'],
                "requirement":  item['candidat'],
                "responsibility": item['vacancyRichText'],
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "salary_str": self.salary_str,
                "location": item["town"]["title"],
                "firm": item["firm_name"],
                "source": "SuperJob"
            })

        return vacancies

    def get_salary(self, salary_from, salary_to, currency):
            if salary_from != None:
                self.salary_from = salary_from
            else:
                self.salary_from = None

            if salary_to != None:
                self.salary_to = salary_to
            else:
                self.salary_to = None

            if self.salary_from != 0 or self.salary_to !=0:
                if self.salary_from != 0:
                    self.salary_str = f'от {self.salary_from} '
                if self.salary_to != 0:
                    self.salary_str = self.salary_str + f'до {self.salary_to}'

                self.salary_str = self.salary_str + f' ({currency})'
            else:
                self.salary_str = "Не указана"
