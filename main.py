import sys
import list_comp
from employee import *
from employee_file_read_write import *
from department import *


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
    dept_list = []
    company = input(
        "Welcome! Type the name of your company to access its database: ").lower()

    employee_file = company+"__employee_info.yaml"

    department_file = company+"__department_info.yaml"

    try:
        emp_list = import_from_yaml(employee_file)
    except Exception:
        print("Employee list for Company "+company +
              " not found, creating new employee list")
    try:
        dept_list = import_from_yaml(department_file)
    except Exception:
        print("Department list for Company "+company +
              " not found, creating new department list")

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
                        # To do: Make a function to create a dept
                        dept_name = input("Enter Employee's department: ")
                        dept_code = input("Enter the dept code")
                        dept_contact_number = input(
                            "Enter the contact num in this format: 123-4567")
                        dept_budget = int(input("Please enter the budget"))
                        dept_company_name = input(
                            "Please enter the company name")
                        new_dept = Department(
                            dept_name, dept_code, dept_contact_number, dept_budget, dept_company_name)
                        dept_list.append(new_dept)
                        # To do: Make this into a function
                        emp_fname = input("Enter first name: ")
                        emp_lname = input("Enter last name: ")
                        emp_doe = input(
                            "Enter date of employment (YYYY MM DD): ")
                        emp_salary = int(input("Enter salary: "))
                        new_emp = Employee(
                            emp_fname, emp_lname, emp_doe, emp_salary, dept_code)
                        emp_list.append(new_emp)
                        try:
                            write_to_yaml(emp_list, employee_file)
                            print("\n~~Employee Succesfully Added!~~")
                        except Exception:
                            print(
                                "Something went wrong with adding employee to file")
                    except:
                        print("Couldn't create the employee")
                    if exitCase('0'):
                        sys.exit()
                    else:
                        continue
                case '2':
                    del_key = input("Enter Employee ID to be removed: ")
                    found = False
                    for emp in emp_list:
                        if Employee.get_id(emp) == del_key:
                            emp_list.remove(emp)
                            found = True
                            print("\n~~Employee Succesfully Removed!~~")
                            break
                    if found:
                        write_to_yaml(emp_list, employee_file)
                    else:
                        print("Employee Not Found")
                    if exitCase('0'):
                        sys.exit()
                    else:
                        continue
                case '3':
                    break
                case '4':
                    list_comp.emp_info(emp_list)

                    if exitCase('0'):
                        sys.exit()
                    else:
                        continue
                # else:
                case _:
                    print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")

        except Exception:
            print("Error, something went wrong. Returning to main menu")


if __name__ == "__main__":
    main()
