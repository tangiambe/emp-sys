import yaml

MAX_YEAR = 2023
MIN_YEAR = 1923
MAX_DAY = 31
MIN_DAY = 1
MAX_MONTH = 12
MIN_MONTH = 1

list_of_employees = []
set_of_emails = set()

class Employee:

    def __init__(self, name: str, dob: str) -> None:
        self.first_name = name.split()[0]
        self.last_name = name.split()[1]
        self.dob = dob
        self.age = 2023 - int(dob[0])
        self.email = create_company_email(self.first_name, self.last_name, self.dob[0])
    
    def __str__(self) -> str:
        return f"{self.first_name}, {self.last_name}, {self.age} years old, born on: {self.dob}, {self.email}"
    
    def get_email(self) -> str:
        return self.email

def ask_for_employee():
    first_name = input("Please enter their first name: ")
    last_name = input("Please enter their last name: ")
    dob = input("Please enter their date of birth in the form YYYY MM DD: ").split()
    return [first_name, last_name, dob]

def validate_names(first_name: str, last_name: str) -> bool:
    if first_name.isalpha() and last_name.isalpha():
        return True
    else:
        return False
    
def validate_dob_format(dob: list) -> bool:
    try: 
        if dob[0].isdigit() and dob[1].isdigit() and dob[2].isdigit:
            return True
        else:
            return False
    except:
        print("Invalid DOB format!")
        print(dob)
        return False

def validate_year(year:str) -> bool:
    year = int(year)
    if year <= MAX_YEAR and year >= MIN_YEAR:
        return True
    else:
        return False
    
def validate_month(month:str) -> bool:
    month = int(month)
    if month <= MAX_MONTH and month >= MIN_MONTH:
        return True
    else:
        return False

def validate_day(day:str, month:str) -> bool:
    day = int(day)
    month = int(month)
    if month == 2 and day <= 28 and day >= MIN_DAY:
        return True
    elif day <= MAX_DAY and day >= MIN_DAY and month != 2:
        return True
    else:
        return False
    
def validate_dob(dob: list) -> bool:
    try: 
        year = dob[0]
        month = dob[1]
        day = dob[2]
        if validate_dob_format(dob) and validate_year(year) and validate_month(month) and validate_day(day, month):
            return True
        else:
            raise Exception("Invalid input(s), are not in the correct range")
    except:
        print("Invalid input format")
        return False
    
def create_company_email(first_name: str, last_name: str, birth_year: str) -> str:
    email = ''
    email = email + first_name + last_name + birth_year[-2:] + "@company.com"
    return email

def create_employee(first_name: str, last_name: str, dob: str) -> Employee:
    employee = Employee(first_name + ' ' + last_name, dob)
    return employee

def write_employee(employees: list):
    # This is the function that writes to the file through yaml calls
    try:
        with open("employee_sheet_yaml.yaml", mode="w", encoding="utf-8") as file:
            yaml.safe_dump_all(employees, file)
    except:
        print("Error occured writing to the file")

def add_employee(employee: list):
    global list_of_employees

    first_name = employee[0]
    last_name = employee[1]
    dob = employee[2]

    if validate_names(first_name, last_name) and validate_dob(dob):
        new_employee = Employee(first_name + ' ' + last_name, dob)

        #if filter_unique(new_employee):
        list_of_employees.append(new_employee)
        
    else:
        pass

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

while True:

    new_employee = ask_for_employee()
    add_employee(new_employee)
    user_quit = input("Quit? ")
    if user_quit == 'Y' or user_quit == 'y':
        break
    else:
        pass

list_of_employees = filter_unique()

write_employee(list_of_employees)