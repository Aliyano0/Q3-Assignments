class Person:
  def __init__(self, name):
    self.name = name

# Inherit class
class Teacher(Person):
  def __init__(self, name, subject_field):
    super().__init__(name)
    self.subject_field = subject_field


# An instance of class Teacher.
teacher = Teacher("Sir Mubashir", "Python")

print(teacher.name)
print(teacher.subject_field)