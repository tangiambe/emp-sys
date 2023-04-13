# Employee Data validation
# This file provides function to check if the date specified as the date of employement or name is correct.

import re
from employee_custom_exception import *

MAX_YEAR = 2023
MIN_YEAR = 1923
MAX_DAY_EVEN = 31
MAX_DAY_ODD = 30
MIN_DAY = 1
MAX_MONTH = 12
MIN_MONTH = 1

def inform_type_error(expected: str, var):
    print(f"Expected a {expected} value, was given a {type(var)}, {var=}")

def inform_value_error(val):
    print(f'Given value ({val}) is not allowed for this field')

def validate_alpha(string: str) -> bool:
    try:
        if string.isalpha():
            return string
        else: raise ValueError
    except TypeError:
        inform_type_error('string', string)
        return False
    except ValueError:
        inform_value_error(string)
        return False
    except:
        print('Error occured with the given val when checking for alpha')
        return False
    
def validate_name(name: str) -> bool:
    try:
        if name == '' or name == ' ' or validate_alpha(name) == False:
            raise NoNameException
        else:
            return True
    except:
        print("Error occured processing the name")

def validate_employee_id(set_of_ids: set, id_to_check: str) -> bool:
    id_sub = set(id_to_check)
    if id_sub.issubset(set_of_ids):
        return False
    else:
        return True
    
def validate_doe(doe: list) -> bool:
    date_split = doe.split()
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]
    try: 
        if year.isdigit() and month.isdigit() and day.isdigit():
            if validate_year(year) and validate_month(month) and validate_day(day, month, year):
                return True
            else: raise Exception
    except:
        print('Invalid Input detected regarding the date. Please check. Format must be a string of YYYY MM DD')
        return False
        
def validate_year(year:str) -> bool:
    try:
        if year.isdigit():
            year = int(year)
            if year <= MAX_YEAR and year >= MIN_YEAR:
                return True
            else:
                raise ValueError
        else:
            raise TypeError
    except TypeError:
        inform_type_error('int', year) 
        print('Expected digit characters in a string for YYYY')
    except ValueError:
        inform_value_error(year)
    except:
        print("Year must be whole number")
    
    return False
        
def validate_month(month:str) -> bool:
    try:
        if month.isdigit():
            month = int(month)
            if month <= MAX_MONTH and month >= MIN_MONTH:
                return True
            else:
                    raise ValueError
        else: raise TypeError
        
    except TypeError:
        print('Expected digit characters in a string for MM')
        inform_type_error('int', month)    
    except ValueError:
        inform_value_error(month)
    except:
        print("Month must be a whole number")
    
    return False

def validate_day(day:str, month:str, year:str) -> bool:
    try:
        if day.isdigit():
            year = int(year)
            day = int(day)
            month = int(month)

            if (year % 4 == 0) and month == 2 and day <= 28 and day >= MIN_DAY:
                return True
            elif (year % 4 != 0) and month == 2 and day <= 27 and day >= MIN_DAY:
                return True
            elif day <= MAX_DAY_ODD and day >= MIN_DAY and ((month % 2 == 1) or month == 12):
                return True
            elif day <= MAX_DAY_EVEN and day >= MIN_DAY and ((month % 2 == 0) and month != 12):
                return True
            else:
                raise ValueError
        else: raise TypeError
        
    except TypeError:
        print('Expected digit characters in a string for DD')
        inform_type_error('int', day)    
    except ValueError:
        inform_value_error(day)
    except:
        print("day must be a whole number")
    
    return False

def validate_salary(salary: str) -> bool:
    try:
        if salary.isdigit():
            salary_value = int(salary)
            if salary_value >= 45000:
                return True
            elif salary_value > 0 and salary_value < 45000:
                print(LowSalaryException(salary))
            else:
                raise ValueError
        else:
            raise TypeError
    except ValueError:
        inform_value_error(salary)
    except TypeError:
        inform_type_error('int', salary)
    except:
        print('Error regarding the given salary')
    
    return False

def validate_budget(budget: str) -> bool:
    try:
        if budget.isdigit():
            budget_value = int(budget)
            if budget_value >= 60000:
                return True
            elif budget_value > 0 and budget_value < 60000:
                print(LowBudgetException(budget))
            else:
                raise ValueError
        else:
            raise TypeError
    except ValueError:
        inform_value_error(budget)
    except TypeError:
        inform_type_error('int', budget)
    except:
        print('Error regarding the given budget')
    
    return False

def phone_match(contact_number: str) -> bool:
    match = re.match(r'([0-9]{3}-[0-9]{4})', contact_number)
    if match is None:
        return False
    else:
        return True

def validate_phone(number: str) -> bool:
    try:
        if phone_match(number):
            return True
        else:
            raise ContactNumberException
    except TypeError:
        inform_type_error('string', number)
    except ContactNumberException:
        print(ContactNumberException(number))
    except:
        print(f"Error detected regarding the given phone number {number=}")
    
    return False