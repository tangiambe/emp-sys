from department import *
from emp_data import *

def dept_name_input() -> str:
    while True:
        dept_name = input("Please enter the department name: ")
        if validate_name(dept_name):
            return dept_name
    
def dept_code_input() -> str:
    dept_code = input("Please input the department code: ")
    return dept_code

def cmp_name_input() -> str:
    while True:
        cmp_name = input("Please enter the company name: ")
        if validate_name(cmp_name):
            return cmp_name
    
def dept_contact_input() -> str:
    while True:
        contact_number = input("Please enter the contact number: ")
        if validate_phone(contact_number):
            return contact_number
    
def dept_budget_input() -> int:
    while True:
        budget = input("Please enter the department budget: ")
        if validate_budget(budget):
            return int(budget)
    
def create_new_department() -> Department:
    
    cmp_name = cmp_name_input()
    dept_name = dept_name_input()
    dept_code = dept_code_input()
    dept_contact = dept_contact_input()
    dept_budget = dept_budget_input()

    return Department(dept_name, dept_code, dept_contact, dept_budget, cmp_name)

def edit_department_name(dept: Department):
    new_name = dept_name_input()
    dept.set_dept_name(new_name)

def edit_department_code(dept: Department):
    print("WARNING YOU ARE EDITING THE DEPARTMENT CODE, THE CHANGES WILL NOT PROPAGATE TO CURRENT EMPLOYEES") # Can be done through list comphrehension
    new_code = dept_code_input()
    dept.set_dept_name(new_code)

def edit_department_contact(dept: Department):
    new_contact = dept_contact_input()
    dept.set_contact(new_contact)

def edit_department_budget(dept: Department):
    new_budget = dept_budget_input()
    dept.set_budget(new_budget)

def edit_company_name(dept: Department):
    new_cmp_name = cmp_name_input()
    dept.set_company_name(new_cmp_name)

def remove_deparment_from_list(dept_list: list, dept_code: str):
    dept_found = search_for_dept(dept_list, dept_code)
    if dept_found is Department:
        dept_list.remove(dept_found)
    else: 
        print("Department not found, nothing was deleted.")

def print_edit_deparments_msg():
    print("What would you like to edit?")
    print("1. Department Name\n2.Department Code\n3. Department Contact Number\n4. Department Budget\n5. Company Name\n0. To Exit\n")

def print_create_department_msg():
    print("You are creating a department")

def print_remove_department_msg():
    print("You are removing a department")

def welcome_dept_menu():
    print("Welcome to the department menu, you may create, edit, or remove departments here.")

def search_for_dept(dept_list: list, dept_code) -> Department:
    for dept in dept_list:
        if dept_code == dept.get_code():
            return dept
    else:
        return None

def edit_department_menu(dept: Department):
    while True:
        choice = input()
        try:
            match choice:
                case '1':
                    edit_department_name(dept)
                case '2':
                    edit_department_code(dept)
                case '3':
                    edit_department_contact(dept)
                case '4':
                    edit_department_budget(dept)
                case '5':
                    edit_company_name(dept)
                case '0':
                    break
                case _:
                    print("Invalid Input")
        except:
            print("Error occurred when editing departments.")


def create_department(dept_list: list):
    print_create_department_msg()
    new_dept = create_new_department()
    dept_list.append(new_dept)
    print(f"Sucessfully created a new department!\n{new_dept}")

def remove_department(dept_list: list):
    print_remove_department_msg()
    remove_deparment_from_list(dept_list, input("Please enter the code of the department you wish to remove: "))

def edit_department(dept_list: list):
    dept_to_edit = search_for_dept(dept_list, input("Please enter the code of the department you wish to edit: "))
    print_edit_deparments_msg()
    edit_department_menu(dept_to_edit)