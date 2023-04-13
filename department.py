class Department:
    
    DEFAULT_NAME = 'default'
    DEFAULT_CODE = 'aaa'
    DEFAULT_CONTACT = '555-5555'
    DEFAULT_BUDGET = 0
    company_name = 'Suraskalas'

    def __init__(self, dept_name = DEFAULT_NAME, dept_code = DEFAULT_CODE, dept_contact_number = DEFAULT_CONTACT, dept_budget = DEFAULT_BUDGET, company_name = company_name) -> None:
        
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.dept_contact = dept_contact_number
        self.budget = dept_budget
        self.company_name = company_name

    def __str__(self) -> str:
        return f"Company: {self.company_name}\nName: {self.dept_name}\nCode: {self.dept_code}\nContact Number: {self.dept_contact}\nBudget: {self.budget}\n"
    
    def get_name(self) -> str:
        return self.dept_name
    def get_code(self) -> str:
        return self.dept_code
    def get_contact(self) -> str:
        return self.dept_contact
    def get_budget(self) -> str:
        return self.budget
    
    def set_dept_name(self, name: str):
        self.dept_name = name
    def set_dept_code(self, code: str):
        self.dept_code = code
    def set_contact(self, contact: str):
        self.dept_contact = contact
    def set_budget(self, budget: int):
        self.budget = budget