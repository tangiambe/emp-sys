import employee

class Department:
    employees = []

    def __init__(self, dept_name: str, dept_code: str, dept_contact_number: str, dept_budget: int, dept_head: employee) -> None:
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.dept_contact = dept_contact_number
        self.budget = dept_budget
        self.dept_head = dept_head
        self.employees.append(dept_head)

    def __str__(self) -> str:
        return f"Name: {self.dept_name}\nCode: {self.dept_code}\nContact Number: {self.dept_contact}\nBudget: {self.budget}\nCurrent Head: {self.dept_head}"
    
    def get_name(self) -> str:
        return self.dept_name
    def get_code(self) -> str:
        return self.dept_code
    def get_contact(self) -> str:
        return self.dept_contact
    def get_budget(self) -> str:
        return self.budget
    def get_dept_head(self) -> employee:
        return self.dept_head
    
    def set_dept_name(self, name: str):
        self.dept_name = name
    def set_dept_code(self, code: str):
        self.dept_code = code
    def set_contact(self, contact: str):
        self.dept_contact = contact
    def set_budget(self, budget: int):
        self.budget = budget
    def set_dept_head(self, head: employee):
        self.dept_head = head