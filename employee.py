import yaml

list_of_employees = []
set_of_emails = set()

class Employee:

    def __init__(self, name: str, doe: str, salary: int, department: str) -> None:
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.doe = doe
        self.salary = salary
        self.department = department
        self.id = create_company_id(self.first_name, self.last_name, self.doe[0])
        self.email = create_company_email(self.first_name, self.last_name, self.doe[0])
    
    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}, {self.doe}, {self.salary}, {self.department}, {self.id}, {self.email}"
    
    def get_email(self) -> str:
        return self.email
    
    def get_first_name(self) -> str:
        return self.first_name
    
    def get_last_name(self) -> str:
        return self.last_name
    
    def get_id(self) -> str:
        return self.id
    
    def get_doe(self) -> str:
        return self.doe
    
    def get_department(self) -> str:
        return self.department
    
    def get_salary(self) -> int:
        return self.salary
    
    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def set_last_name(self, last_name: str):
        self.first_name = last_name

    def set_id(self, id: str): #manually set a special id
        self.id = id
    
    def set_doe(self, doe: str):
        self.doe = doe
    
    def set_department(self, department:str): # this needs to be changed after to reflect the department class
        self.department = department

    def set_salary(self, salary: int):
        self.salary = salary

def create_company_email(first_name: str, last_name: str, employment_year: str) -> str:
    email = ''
    email = email + first_name.lower() + last_name.lower() + employment_year[-2:] + "@company.com"
    return email

def create_company_id(first_name: str, last_name: str, year: str):
    initials = first_name.lower()[0] + last_name.lower()[0]
    year_joined = year[-2:]

    return initials + year_joined