import employee

class Department:
    employees = []
    DEFAULT_NAME = 'default'
    DEFAULT_CODE = 'aaa'
    DEFAULT_CONTACT = '555-5555'
    DEFAULT_BUDGET = 0
    DEFAULT_HEAD = None

    def __init__(self, dept_name = DEFAULT_NAME, dept_code = DEFAULT_CODE, dept_contact_number = DEFAULT_CONTACT, dept_budget = DEFAULT_BUDGET, dept_head = DEFAULT_HEAD) -> None:
        
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.dept_contact = dept_contact_number
        self.budget = dept_budget
        self.dept_head = dept_head
        if dept_head is not None:
            self.employees.append(dept_head)
        else:
            pass

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