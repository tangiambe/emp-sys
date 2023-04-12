import sys
from employee import *
from employee_file_read_write import *


def menu_choices():
    print("\n************* Employee Management System ***************")
    print("1) Add Employee          2) Remove Employee")
    print("3) Update Employee       4) List Employee Information")
    print("0) Log Out")

def exitCase(exit_key: str):
    if input(f"\nEnter any key to return to Menu. ({exit_key} to Log Out): ") == exit_key:
        print("Logging Out.....Bye Bye!")
        return True

def main():
    emp_list = []
    company = input("Welcome! Type the name of your company to access its database: ").lower()
    
    employee_file = company+"__employee_info.yaml"

    department_file = company+"__department_info.yaml"

    try:
        emp_list = import_from_yaml(employee_file)
    except Exception:
        print("Employee list for Company "+company+" not found, creating new employee list")
    try:
        dept_list = import_from_yaml(department_file)
    except Exception:
        print("Department list for Company "+company+" not found, creating new department list")
    
    while True:
        menu_choices()
        option = input("\nPick an option: ")
        try:
            match option:
                case '0':
                    print("Logging Out......Bye Bye!")
                    sys.exit()
                case '1':
                    try:
                        emp_fname = input("Enter first name: ")
                        emp_lname = input("Enter last name: ")
                        emp_doe = input ("Enter date of employment (YYYY MM DD): ")
                        emp_salary = int(input("Enter salary: "))
                        emp_dept = input ("Enter Employee's department: ")
                        new_emp = Employee(emp_fname, emp_lname, emp_doe, emp_salary, emp_dept)
                        emp_list.append(new_emp)
                        try:
                            write_to_yaml(emp_list, employee_file)
                        except Exception:
                            print("Something went wrong with adding employee to file")
                    except Exception:
                        print("Error, something went wrong with adding employee")
                    
                    if exitCase('0'):
                        sys.exit()
                    else: 
                        continue
                case '4':
                    emp_list = import_from_yaml(employee_file)
                    for emp in emp_list:
                        print(emp)
                        
                    if exitCase('0'):
                        sys.exit()
                    else: 
                        continue
                #else:
                case _:
                    print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")

        except Exception:
            print("Error, something went wrong. Returning to main menu")



main()
            

