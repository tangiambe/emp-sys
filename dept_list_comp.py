from datetime import datetime
from employee import *
from main import *


def dept_info_menu():
    print("\n************* Department Information ***************")
    print("1) All Departments           2) Select Department")
    print("0) Back to Department Management")


def dept_info(dept_list):
    """
    Filter Dept Info by:
      - show all depts names
      - show one dept info
    """
    while True:
        dept_info_menu()
        info = input("\nChoose an option: ")
        match info:
            case '0':
                break
            case '1':
                print(f"\nThere are {len(dept_list)} departments:\n")
                for dept in dept_list:
                    print(dept.get_name())
            case '2':
                select_dept(dept_list)


def select_dept(dept_list):
    try:
        user_dept = str(input("Enter the department name: "))
        for dept in dept_list:
            if (user_dept in dept.get_name()):
                cnt = 1
                print(f"\n{dept}")
        if cnt != 1:
            raise Exception
    except Exception:
        print("That department does not exist.")


if __name__ == "__main__":
    dept1 = Department("Name", "code", "###-####", 100, "cognixia")
    dept2 = Department("janitor", "jan", "123-####", 1000, "cognixia")
    dept3 = Department("driver", "dri", "321-####", 2500, "amazon")
    dept4 = Department("Sales", "sal", "123-4568", 2020, "company")

    dept_info(dept_list=[dept1, dept2, dept3, dept4])
    pass
