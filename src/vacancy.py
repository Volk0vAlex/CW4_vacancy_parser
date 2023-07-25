class Vacancy:
    def __init__(self, job_id, job_name, job_url, salary_from, salary_to, salary_str, requirements, responsibility, location, firm_name):
        self.id = job_id
        self.job_name = job_name
        self.job_url = job_url

        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_str = salary_str

        self.requirements = requirements
        self.responsibility = responsibility
        self.location = location
        self.firm_name = firm_name

    @classmethod
    def __validate_salary(cls, p_salary):
        if p_salary < 0:
            return False
        else:
            return True

    def __lt__(self, other):
        if other.salary_from is None:
            other_salary_from = 0
        else:
            other_salary_from = other.salary_from

        if self.salary_from is None:
            self_salary_from = 0
        else:
            self_salary_from = self.salary_from

        return self_salary_from < other_salary_from

    def __gt__(self, other):
        if other.salary_from is None:
            other_salary_from = 0
        else:
            other_salary_from = other.salary_from

        if self.salary_from is None:
            self_salary_from = 0
        else:
            self_salary_from = other_salary_from

        return self_salary_from > other_salary_from

    def __eq__(self, other):
        if other.salary_from is None:
            other_salary_from = 0
        else:
            other_salary_from = other.salary_from

        if self.salary_from is None:
            self_salary_from = 0
        else:
            self_salary_from = self.salary_from

        return self_salary_from == other_salary_from

    def __str__(self):
        return f"Вакансия: {self.job_name}\nЗарплата:{self.salary_str}\nURL:{self.job_url}\nГород: {self.location}\nОрганизация: {self.firm_name}\nТребования:{self.requirements}\n"
