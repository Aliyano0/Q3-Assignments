class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print(f"Woof! The dog name is {self.name}")


dog1 = Dog("Khalid Al-Kashmiri", "Siberian Husky")

dog1.bark()