# Employee Data validation
# This file provides function to check if the date specified as the date of employement or name is correct.

MAX_YEAR = 2023
MIN_YEAR = 1923
MAX_DAY = 31
MIN_DAY = 1
MAX_MONTH = 12
MIN_MONTH = 1

def validate_names(full_name: str) -> bool:
    name_split = full_name.split()
    first_name = name_split[0]
    last_name = name_split[1]
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
            if validate_year(year) and validate_month(month) and validate_day(day, month):
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

def validate_day(day:str, month:str) -> bool:
    try:
        day = int(day)
        month = int(month)
        if month == 2 and day <= 28 and day >= MIN_DAY:
            return True
        elif day <= MAX_DAY and day >= MIN_DAY and month != 2:
            return True
        else:
            raise ValueError
        
    except ValueError:
        print(f"Day ({day}) is not within range of the specicifed month ({month})")
    except:
        print(f"Day must be an integer. (Was given {day})")