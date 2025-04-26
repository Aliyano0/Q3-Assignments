class Employee:
  name = "Aliyan"
  _salary = "20K USD"
  __ssn = "123456789"

  def __init__(self):
    pass

new_employee = Employee()
print(new_employee.name) # It prints the public variable.
print(new_employee._salary) # It prints the private variable. 
print(new_employee.__ssn) # Accessing Private variable throws an attribute error because we can access it within the Class or we can also access it through a class method.(Getter method)