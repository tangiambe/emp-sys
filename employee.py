import department

class Employee:

    def __init__(self, first_name: str, last_name: str, doe: str, salary: int, dept: department) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.doe = doe
        self.salary = salary
        self.department = dept
        self.id = create_company_id(self.first_name, self.last_name, self.doe)
        self.email = create_company_email(self.first_name, self.last_name, self.doe[2:4])
    
    def __str__(self) -> str:
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nDate of Employment: {self.doe}\nSalary: {self.salary}\nID: {self.id}\nEmail: {self.email}"
    
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
    
    def get_department(self) -> department:
        return self.department
    
    def get_salary(self) -> int:
        return self.salary
    
    def set_first_name(self, first_name: str):
        self.first_name = first_name.capitalize()

    def set_last_name(self, last_name: str):
        self.first_name = last_name.capitalize()

    def set_id(self, id: str): #manually set a special id
        self.id = id
    
    def set_doe(self, doe: str):
        self.doe = doe
    
    def set_department(self, dept: department): # this needs to be changed after to reflect the department class
        self.department = dept

    def set_salary(self, salary: int):
        self.salary = salary

def create_company_email(first_name: str, last_name: str, doe: str) -> str:
    email = ''
    email = email + first_name.lower() + '.' + last_name.lower() + doe[2:4] + "@company.com"
    return email

def create_company_id(first_name: str, last_name: str, doe: str) -> str:
    initials = first_name.lower()[0] + last_name.lower()[0]
    year_joined = doe[2:4]

    return initials + year_joined