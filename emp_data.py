# Employee Data validation
# This file provides function to check if the date specified as the date of employement or name is correct.

import re

MAX_YEAR = 2023
MIN_YEAR = 1923
MAX_DAY_EVEN = 31
MAX_DAY_ODD = 30
MIN_DAY = 1
MAX_MONTH = 12
MIN_MONTH = 1

def validate_names(first_name: str, last_name: str) -> bool:
    if first_name.isalpha() and last_name.isalpha():
        return True
    else:
        return False
    
def validate_doe(doe: list) -> bool:
    date_split = doe.split()
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]
    try: 
        if year.isdigit() and month.isdigit() and day.isdigit():
            if validate_year(year) and validate_month(month) and validate_day(day, month, year):
                return True
            else:
                raise ValueError
        else:
            raise TypeError
    except TypeError:
        print("Invalid DOB format! Please Enter Numbers")
        return False
    except ValueError:
        print("Invalid numbers, please enter appropriate numbers within the range")
        return False
    except:
        return False

def validate_year(year:str) -> bool:
    try:
        year = int(year)
        if year <= MAX_YEAR and year >= MIN_YEAR:
            return True
        else:
            raise ValueError
        
    except ValueError:
        print("Year is not a acceptable number")
        return False
    except:
        print("Year must be an integer")
        return False
    
def validate_month(month:str) -> bool:
    try:
        month = int(month)
        if month <= MAX_MONTH and month >= MIN_MONTH:
            return True
        else:
                raise ValueError
        
    except ValueError:
        print("Year is not a acceptable number")
        return False
    except:
        print("Year must be an integer")
        return False

def validate_day(day:str, month:str, year:str) -> bool:
    try:
        year = int(year)
        day = int(day)
        month = int(month)

        if (year % 4 == 0) and month == 2 and day <= 28 and day >= MIN_DAY:
            return True
        elif (year % 4 != 0) and month == 2 and day <= 27 and day >= MIN_DAY:
            return True
        elif day <= MAX_DAY_ODD and day >= MIN_DAY and (month % 2 == 1):
            return True
        elif day <= MAX_DAY_EVEN and day >= MIN_DAY and (month % 2 == 0):
            return True
        else:
            raise ValueError
        
    except ValueError:
        print(f"Day ({day}) is not within range of the specicifed month ({month})")
    except:
        print(f"Day must be an integer. (Was given {day})")

def validate_salary(salary: int) -> bool:
    try:
        if salary is int and salary > 0:
            return True
        elif salary is int and salary < 0:
            raise ValueError
        else:
            raise TypeError
    except ValueError:
        print(f"Negative value detected for salary! Was given: {salary}")
    except TypeError:
        print(f"Wring type, expected integer. Got a {type(salary)}")

def validate_phone(number: str) -> bool:
    phone_format = re.compile(r'[0-9]{3}-[0-9]{4}')
    try:
        if phone_format.search(number):
            return True
        else:
            return False
    except TypeError:
        print("Wrong type! Expected String in 000-0000 format")
    except:
        print("Error detected")