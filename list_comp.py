import sys
from datetime import datetime
from employee import *
from main import *


def emp_info_menu():
    print("\n************* Employee Information ***************")
    print("1) Years of Employment     2) Salary")
    print("3) Department              4) All Employee Information")
    print("0) Back to Employee Menu")


def emp_info(emp_list):
    """
    Using list comprehension filtered by:
        - date of employment (doe)
        - salary
        - department?
    """
    while True:
        emp_info_menu()
        info = input("\nFilter by: ")
        match info:
            case '0':
                break
            case '1':
                doe_filter()
            case '2':
                sal_filter()
            case '3':
                dept_filter()
            case '4':
                print(f"There are {len(emp_list)} employees:\n")
                for emp in emp_list:
                    print(emp, "\n")


def doe_filter():
    todays_date = datetime.today().strftime('%Y %m %d')
    today = datetime.strptime(todays_date, "%Y %m %d")

    # if employed in the past year
    one_year = [emp.get_id() for emp in emp_list if (
        (today - datetime.strptime(emp.get_doe(), "%Y %m %d"))/365).days < 1]
    print(len(one_year), "people were hired in the past year:")
    for i in one_year:
        print(i + " ", end="")
    print("were all hired in the past year.\n")

    # if employed for ten-19 years
    ten_year = [emp.get_id() for emp in emp_list if 10 <= (
        (today - datetime.strptime(emp.get_doe(), "%Y %m %d"))/365).days < 20]
    print(len(ten_year), "people have been employed for 10 - 19 years:")
    for i in ten_year:
        print(i + " ", end="")
    print("have all been employed for 10 - 19 years.\n")

    # if employed for 20+ years
    twenty_year = [emp.get_id() for emp in emp_list if (
        (today - datetime.strptime(emp.get_doe(), "%Y %m %d"))/365).days >= 20]
    print(len(twenty_year), "people have been employed for 20+ years:")
    for i in twenty_year:
        print(i + " ", end="")
    print("have all been employed for 20+ years.\n")


def sal_filter():
    # salary < 50K
    sal_50 = [emp.get_id()
              for emp in emp_list if (emp.get_salary() < 50000)]
    print(f"\n{len(sal_50)} people have a salary below $50K:")
    for i in sal_50:
        print(i + " ", end="")
    print("have a salary below $50K.\n")
    # 50K < salary < 100K
    sal_50_100 = [emp.get_id()
                  for emp in emp_list if (50000 < emp.get_salary() < 100000)]
    print(f"{len(sal_50_100)} people have a salary between $50K and $100K:")
    for i in sal_50_100:
        print(i + " ", end="")
    print("have a salary between $50K and $100K.\n")
    # 100K < salary
    sal_100 = [emp.get_id()
               for emp in emp_list if (emp.get_salary() >= 100000)]
    print(f"{len(sal_100)} people have a salary of $100K or higher:")
    for i in sal_100:
        print(i + " ", end="")
    print("have a salary of $100K or higher.\n")


def dept_filter():
    # every emp has department code
    # ask user for dept code
    # show all emps that have that dept code
    pass


if __name__ == "__main__":
    emp1 = Employee("Alessi", "Reiter", "2022 05 12", 50000, "python")
    emp2 = Employee("billy", "bob", "2000 03 12", 75000, "java")
    emp3 = Employee("first", "last", "2020 02 01", 35000, "math")
    emp4 = Employee("one", "two", "1998 02 01", 35000, "cs")
    emp5 = Employee("John", "Doe", "2003 02 01", 35000, "professor")
    emp6 = Employee("Jane", "Doe", "2010 02 01", 35000, "janitor")
    emp7 = Employee("jack", "black", "2022 07 12", 100000, "python")
    emp8 = Employee("sam", "pucket", "2022 12 12", 120000, "python")

    emp_list = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8]
    emp_info(emp_list)
