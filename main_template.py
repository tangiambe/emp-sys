import sys
# from employee import *
# from employee_file_read_write import *


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
    print("3) Update Department       4) List Department Information")
    print("0) Return to Main Menu")

    

def main():
    emp_list = []
    company = input("Welcome! Type the name of your company to access its database: ").lower()
    
    employee_file = company+"__employee_info.yaml"

    department_file = company+"__department_info.yaml"
    
    # main_menu(company)
    
    # try:
    #     emp_list = import_from_yaml(employee_file)
    # except Exception:
    #     print("\nEmployee list for Company "+company+" not found, creating new employee list")
    # try:
    #     dept_list = import_from_yaml(department_file)
    # except Exception:
    #     print("\nDepartment list for Company "+company+" not found, creating new department list")
    
    while True:
        main_menu(company)
        option = input("\nPick an option: ")
        match option:
            #TERMINATES PROGRAM
            case '0':
                print("Logging Out......Bye Bye!")
                sys.exit()
           
            # EMPLOYEE MENU
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
                            # add_emp()
                            
                            input("\nEnter any key to return to Employee Menu. ")
                            print("Returning to Employee Menu.....")
                            continue
                        case '2':
                            # REMOVE EMPLOYEE
                            # remove_emp()
                            
                            input("\nEnter any key to return to Employee Menu. ")
                            print("Returning to Employee Menu.....")
                            continue
                        case '3':
                            # UPDATE EMPLOYEE
                            # update_emp()
                            
                            input("\nEnter any key to return to Employee Menu. ")
                            print("Returning to Employee Menu.....")
                            continue
                        case '4':
                            # LIST EMPLOYEE INFO (LIST COMPREHENSION)
                            # list_emp()
                            
                            input("\nEnter any key to return to Employee Menu. ")
                            print("Returning to Employee Menu.....")
                            continue
                        case _:
                            print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")
            
            #DEPARTTMENT MENU
            case '2':
                while True:
                    dept_menu()
                    option = input("\nPick an option: ")
                    match option:
                        case '0':
                            print("Returning to Main Menu......")
                            break
                        case '1':
                            # ADD DEPARTMENT
                            # add_dept()
                            
                            input("\nEnter any key to return to Department Menu. ")
                            print("Returning to Department Menu.....")
                            continue
                        case '2':
                            # REMOVE DEPARTMENT
                            # remove_dept()
                            
                            input("\nEnter any key to return to Department Menu. ")
                            print("Returning to Department Menu.....")
                            continue
                        case '3':
                            # UPDATE DEPARTMENT
                            # update_dept()
                            
                            input("\nEnter any key to return to Department Menu. ")
                            print("Returning to Department Menu.....")
                            continue
                        case '4':
                            # LIST DEPARTMENT INFO (OPTIONAL LIST COMPREHENSION)
                            # list_dept()
                            
                            input("\nEnter any key to return to Department Menu. ")
                            print("Returning to Department Menu.....")
                            continue
                        case _:
                            print("~Error: Invalid Input! PLEASE ENTER A VALID OPTION.~\n")
                

main()
