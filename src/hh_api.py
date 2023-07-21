from abstract import GetVacanciesAbstractClass
import requests

class HeadHunter(GetVacanciesAbstractClass):
    """ Создан класс для получения вакансий с hh.ru """
    url: str = 'https://api.hh.ru'

    def __init__(self, keyword):
        self.salary_str = None
        self.__params = {
            "text": keyword,
            "page": 0,
            "per_page": 100
        }
        self.vacancies_url = self.url + "vacancies"
        self.__full_vacancies = []
        self.salary_from = None
        self.salary_to = None

    def get_vacancies(self, page_count=1):
        page = self.__params["page"]
        while page < page_count:
            print(f"HeadHunter, Страница {page+1}", end=": ")
            vacancies_list = self.get_request()
            print(f"Найдено {len(vacancies_list)}")

            self.__full_vacancies.extend(vacancies_list)
            page += 1
            self.__params["page"] = page

        vacancies_list = self.get_vacancy_info()
        return vacancies_list

    def get_request(self):
        response = requests.get(self.vacancies_url, params=self.__params)

        return response.json()["items"]

    def get_salary(self, salary):
        if salary != None:
            if salary["from"] != None:
                self.salary_from = salary["from"]
            else:
                self.salary_from = None

            if salary["to"] != None:
                self.salary_to = salary["to"]
            else:
                self.salary_to = None

            self.salary_str = f'от {self.salary_from} до {self.salary_to} ({salary["currency"]}) Гросс: {salary["gross"]}'
        else:
            self.salary_from = None
            self.salary_to = None
            self.salary_str = "Не указана"

    def get_vacancy_info(self):
        vacancies = []
        for item in self.__full_vacancies:
            self.get_salary(item["salary"])
            vacancies.append({
                "id": item["id"],
                "job_name": item["name"],
                "job_url": item["alternative_url"],
                "requirement": item['snippet']["requirement"],
                "responsibility": item['snippet']["responsibility"],
                "salary_from": self.__salary_from,
                "salary_to": self.salary_to,
                "salary_str": self.salary_str,
                "location": self.get_adress(item["adress"]),
                "firm": item["employer"]["name"],
                "source": "HeadHunter"
            })

        return vacancies

    def get_address(self, address):
        if address != None:
            return address["city"]
        else:
            return "Не указан"
