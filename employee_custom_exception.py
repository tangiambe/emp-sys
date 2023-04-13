from employee import *

class NoNameException(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return("Employee" + self.name + " does not have an appropriate name!")
    
class LowBudgetException(Exception):
    def __init__(self, budget):
        self.budget = budget
    def __str__(self):
        return("Budget of "+ self.budget +" is too low to be assigned as a budget for a department!")
    
class LowSalaryException(Exception):
    def __init__(self, salary):
        self.salary = salary
    def __str__(self):
        return("Salary of "+ self.salary +" is too low to be assigned to an employee!")
    
class ContactNumberException(Exception):
    def __init__(self, number):
        self.number = number
    def __str__(self):
        return("The number given "+ self.number +" does not follow the correct format! Must be 123-4567")
