class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_info(self):
        print(f"Department: {self.dept_name}, Employee: {self.employee.name}")


emp1 = Employee("Ali")  

dept1 = Department("HR", emp1)  

dept1.show_info() 
