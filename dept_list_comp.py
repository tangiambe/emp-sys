from datetime import datetime
from employee import *
from main import *


def dept_info_menu():
    print("\n************* Department Information ***************")
    print("1) All Departments    2) Select Department")
    print("3)               4) ")
    print("0) Back to Main Menu")


def dept_info(dept_list):
    """
    Using list comprehension filtered by:
        - date of employment (doe)
        - salary
        - department?
    """
    while True:
        dept_info_menu()
        info = input("\nSearch by: ")
        match info:
            case '0':
                main()
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                print(f"There are {len(emp_list)} employees:\n")
                for emp in emp_list:
                    print(emp, "\n")
