from employee import *
from employee_file_read_write import *
from department import *
from dept_menu_functions import *

def emp_name_input() -> str:
    while True:
        emp_name = input("Please enter the employee's first/last name: ")
        if validate_name(emp_name):
            return emp_name
    
def emp_id_input() -> str:
    emp_id = input("Please input the department code: ")
    return emp_id

def emp_doe_input() -> str:
    while True:
        emp_doe = input("Please input the department code: ")
        if validate_doe(emp_doe):
            return emp_doe

def emp_new_dept_input() -> str:
    while True:
        emp_new_dept = input("Please enter ")
        # check dept codes to see if one exists
        # if yes return the input

def emp_salary_input() -> int:
    while True:
        salary = input("Please enter the department budget: ")
        if validate_salary(salary):
            return int(salary)

def add_emp_prompt(emp_list, employee_file, dept_list, dept_file):
    emp_fname = input("Enter first name: ")
    emp_lname = input("Enter last name: ")
    emp_doe = input ("Enter date of employment (YYYY MM DD): ")
    emp_salary = int(input("Enter salary: "))
    dept_code = input("Enter the dept code: ")
    return(add_emp(emp_list, employee_file,emp_fname,emp_lname,emp_doe,emp_salary,verify_dept(dept_code, dept_list, dept_file)))

def verify_dept(code, dept_list, dept_file):
    dept_found = False
    while not dept_found:
        for dept in dept_list:
            if Department.get_code(dept) == code:
                dept_found = True
                return code
        if not dept_found:
            print(f"Department '{code}' does not exist!\nAssigning DEFAULT Department...")  
            code = Department.DEFAULT_CODE
            dept_list.append(Department(dept_code= code))
            try:
                write_to_yaml(dept_list, dept_file)
            except Exception:
                print("Something went wrong with adding DEFAULT department to file")
            return code   
        else:
            print("Invalid Input!\n")
            break

def add_emp(emp_list, employee_file,emp_fname,emp_lname,emp_doe,emp_salary,dept_code):
    new_emp = Employee(emp_fname, emp_lname, emp_doe, emp_salary, dept_code)
    emp_list.append(new_emp)
    try:
        write_to_yaml(emp_list, employee_file)
    except Exception:
        print("Something went wrong with adding employee to file")
    return emp_list



def remove_emp(del_key,emp_list,employee_file):

    found = False
    for emp in emp_list:
            if Employee.get_id(emp) == del_key:
                emp_list.remove(emp)
                found = True
                break
    if found:
            write_to_yaml(emp_list, employee_file)
    else:
        print("Employee Not Found")
    return emp_list

def update_emp(emp_list,employee_file):
    employee_id = input("Input the ID of the employee that you would like to update: ")
    count = 0

    #Search for employees
    while(count < len(emp_list)):
        Employee = emp_list[count]
        emp_list_id = Employee.get_id()
        if (emp_list_id == employee_id):
            #Employee found
            count = len(emp_list) + 1

            #Get current values
            emp_fname = Employee.get_first_name()
            emp_lname = Employee.get_last_name()
            emp_doe = Employee.get_doe()
            emp_salary = Employee.get_salary()
            dept_code = Employee.get_department()

            selection = True

            #Determine which values to change
            while (selection == True):
                print("\nWhich field would you like to edit?")
                print("1: First Name")
                print("2: Last Name")
                print("3: Date of Employment")
                print("4: Salary")
                print("5: Dept. Code")
                print("Type any other key to exit")

                choice = input("")

                if (choice == "1"):
                    emp_fname = input("Enter new first name: ")
                    print("\nFirst name edited!\n")
                elif(choice == "2"):
                    emp_lname = input("Enter new last name: ")
                    print("\nLast name edited!\n")
                elif(choice == "3"):
                    emp_doe = input ("Enter new date of employment (YYYY MM DD): ")
                    print("\nEmployment date edited!\n")
                elif(choice == "4"):
                    emp_salary = int(input("Enter new salary: "))
                    print("\nSalary edited!\n")
                elif(choice == "5"):
                    dept_code = input("Enter the new dept code: ")
                    print("\nDepartment code edited!\n")
                else:
                    selection = False

            
            #Update by purging old employee, adding new employee with updated info
            emp_list = remove_emp(employee_id,emp_list,employee_file)
            emp_list = add_emp(emp_list, employee_file,emp_fname,emp_lname,emp_doe,emp_salary,dept_code)
            
            return(emp_list)
        else:
            count = count + 1
            
    #Employee not found, return to main meny
    print("Error, employee not found!")
    return emp_list
    

def list_emp(emp_list):
    for emp in emp_list:
        print(f"\n{emp}")
