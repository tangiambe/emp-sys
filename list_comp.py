from datetime import datetime
import employee


def list_comp(emp_list):
    """
    Using list comprehension - filter by date employ
    """
    todays_date = datetime.today().strftime('%Y %m %d')

    # convert string to date object
    today = datetime.strptime(todays_date, "%Y %m %d")

    # if employed in the past year
    one_year = [emp for emp in emp_list if (
        (today - datetime.strptime(emp.get_doe(), "%Y %m %d"))/365).days < 1]

    # if employed for ten+ years
    ten_year = [emp for emp in emp_list if (
        (today - datetime.strptime(emp.get_doe(), "%Y %m %d"))/365).days >= 10]


emp1 = employee.Employee("Alessi Reiter", "2022 05 12", 50000, "python")
emp2 = employee.Employee("billy bob", "2000 03 12", 75000, "java")
emp3 = employee.Employee("first last", "2020 02 01", 35000, "math")
emp_list = [emp1, emp2, emp3]

list_comp(emp_list)
