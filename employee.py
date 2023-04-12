import yaml

list_of_employees = []
set_of_emails = set()

class Employee:

    def __init__(self, name: str, doe: str, salary: int, department: str) -> None:
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.doe = doe
        self.age = 2023 - int(dob[0])
        self.salary = salary
        self.department = department
        self.id = #user create id function here
        self.email = create_company_email(self.first_name, self.last_name, self.dob[0])
    
    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}, {self.age} years old, born on: {self.dob}, {self.email}"
    
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

def ask_for_employee():
    first_name = input("Please enter their first name: ")
    last_name = input("Please enter their last name: ")
    dob = input("Please enter their date of birth in the form YYYY MM DD: ").split()
    return [first_name, last_name, dob]
    
def create_company_email(first_name: str, last_name: str, birth_year: str) -> str:
    email = ''
    email = email + first_name + last_name + birth_year[-2:] + "@company.com"
    return email

def write_employee(employees: list):
    # This is the function that writes to the file through yaml calls
    try:
        with open("employee_sheet_yaml.yaml", mode="w", encoding="utf-8") as file:
            yaml.safe_dump_all(employees, file)
    except:
        print("Error occured writing to the file")

def filter_unique():
    global list_of_employees
    global set_of_emails

    unique_list = []

    for employee in list_of_employees:
        if employee.get_email() not in set_of_emails:
            set_of_emails.add(employee.get_email())
            unique_list.append(employee)
        else:
            print("Duplicate Purged")
            pass
    
    return unique_list