import yaml
from employee import *


def write_to_yaml(employeeList,fileName):
    #Will write an object list to a .yaml file)
    with open (fileName,"wt") as file:
        data = yaml.dump(employeeList,sort_keys = False)
        file.write(data)

def import_from_yaml(fileName):
    #Will open a .yaml file and return a list of objects)
    with open (fileName,"rt") as file:
        data = yaml.load(file,Loader = yaml.Loader)
    return data

def generate_id_set(emp_list):
    #Will take an employee list and generate a
    #set of all current employee ID's
    count = 0
    generated_set = set()
    while(count < len(emp_list)):
        generated_set.add(emp_list[count].get_id())
        count = count + 1
    return(generated_set)


