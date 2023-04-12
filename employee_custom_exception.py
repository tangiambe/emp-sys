from employee import *

class NoLastNameException(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return("Employee"+self.name+" does not have a last name!")
