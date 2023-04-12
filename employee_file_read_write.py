import yaml
from employee import *


def write_to_yaml(employeeList,fileName):
    with open (fileName,"wt") as file:
        data = yaml.dump(employeeList,sort_keys = False)
        file.write(data)

def import_from_yaml(fileName):
    with open (fileName,"rt") as file:
        data = yaml.load(file,Loader = yaml.Loader)
    return data



