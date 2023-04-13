import sys
import os
import emp_list_comp
from employee import *
from employee_file_read_write import *
from department import *
from dept_menu_functions import *
from employee_add_subtract import *

emp_list = []
dept_list = []


def main_menu(company_name: str):
    print(f"\n************ {company_name.capitalize()} Management System ***************")
    print("\n1) Manage Employees          2) Manage Departments             0) Log Out\n")


def emp_menu():
    print("\n************* Employee Management ***************")
    print("1) Add Employee          2) Remove Employee")
    print("3) Update Employee       4) List Employee Information")
    print("0) Return to Main Menu")
        
def dept_menu():
    print("\n************* Department Management ***************")
    print("1) Add Department          2) Remove Department")
    print("3) Update Departmentt      4) List Department Information")
    print("0) Return to Main Menu")



def main():
    global emp_list
    global dept_list

    
    company = input("Welcome! Type the name of your company to access its database: ").lower()
    
    employee_file = company+"/"+company+"__employee_info.yaml"

    department_file = company+"/"+company+"__department_info.yaml"

    try:
        emp_list = import_from_yaml(employee_file)
    except Exception:
        print("Employee list for Company "+company+" not found, creating new employee list")
        os.mkdir(company)
    
    try:
        dept_list = import_from_yaml(department_file)
    except Exception:
        print("Department list for Company "+company+" not found, creating new department list")

    while True:
        main_menu(company)
        option = input("\nPick an option: ")
        try:
            match option:
                case '0':
                    print("Logging Out......Bye Bye!")
                    sys.exit()
                    
                #EMPLOYEE MENU
                case '1':
                    while True:
                        emp_menu()
                        option = input("\nPick an option: ")
                        match option:
                            case '0':
                                print("Returning to Main Menu......")
                                break
                            case '1':
                                # ADD EMPLOYEE
                                try:
                                    add_emp_prompt(emp_list, employee_file, dept_list, department_file)
                                except:
                                    print("Couldn't create the employee")    
                                input("\nEnter any key to return to Employee Menu: ")
                                print("Returning to Employee Menu.....")
                                continue
                            case '2':
                                # REMOVE EMPLOYEE
                                del_key = input("Enter Employee ID to be removed: ")
                                remove_emp(del_key,emp_list,employee_file)
                                input("\nEnter any key to return to Employee Menu: ")
                                print("Returning to Employee Menu.....")
                                continue
                            case '3':
                                # UPDATE EMPLOYEE
                                update_emp(emp_list,employee_file)
                                input("\nEnter any key to return to Employee Menu: ")
                                print("Returning to Employee Menu.....")
                                continue
                            case '4':
                                # LIST EMPLOYEE INFO (LIST COMPREHENSION)
                                emp_list_comp.emp_info(emp_list)
                                print("Returning to Employee Menu.....")
                                continue
                            case _:
                                print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")
  
                #DEPARTMENT MENU
                case '2':
                    while True:
                        dept_menu()
                        option = input("\nPick an option: ")
                        match option:
                            case '0':
                                print("Returning to Main Menu......")
                                break
                            case '1':
                                # ADD DEPARTMENTT
                                create_department(dept_list)
                                try:
                                    write_to_yaml(dept_list, department_file)
                                except Exception:
                                    print("Something went wrong with adding department to file")    
                                input("\nEnter any key to return to Department Menu. ")
                                print("Returning to Department Menu.....")
                                continue
                            case '2':
                                # REMOVE DEPARTMENT
                                remove_department(dept_list)
                                input("\nEnter any key to return to Department Menu. ")
                                print("Returning to Department Menu.....")
                                continue
                            case '3':
                                # UPDATE DEPARTMENT
                                edit_department(dept_list)
                                input("\nEnter any key to return to Department Menu. ")
                                print("Returning to Department Menu.....")
                                continue
                            case '4':
                                # LIST DEPARTMENT INFO (OPTIONAL LIST COMPREHENSION)
                                list_department(dept_list)
                                input("\nEnter any key to return to Department Menu. ")
                                print("Returning to Departmentt Menu.....")
                                continue
                            case _:
                                print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")

        except Exception:
            print("Error, something went wrong. Returning to main menu")

if __name__ == "__main__":
    main()