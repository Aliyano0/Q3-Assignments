
# # class Vehicle:
# #     def start(self):
# #         print("Starting vehicle")

# # class Car(Vehicle):
# #     def start(self):
# #         super().start()
# #         print("Starting car")

# # class ElectricCar(Car):
# #     def start(self):
# #         print("Starting electric car silently")

# # ev = ElectricCar()
# # ev.start()

# # class A:
# #     def show(self):
# #         print("A")

# # class B(A):
# #     def show(self):
# #         super().show()
# #         print("B")

# # B().show()


# class Product:
#     def __init__(self, price, product):
#         self._product = product
#         self.__price = price


#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self.__price = value
    


# c = Product(100, 2)

# print(c._product)

# 1.
# class Library:
#   total_books = 0
#   def __init__(self,name: str):
#     self.name = name
#     self.book_list = []

#   def add_book(self, book_name):
#     self.book_list.append(book_name)
#     Library.total_books += 1
#     print("Book added.")

#   def show_books(self):
#     print(f"Total Books: {self.total_books}")
#     for book in self.book_list:
#       print(book)


# library1 = Library("First")
# library2 = Library("Second")
# library1.add_book("Hello")
# library2.add_book("Hi")
# library2.show_books()


# 2. 
# class House:
#   def __init__(self):
#     self.rooms_list = []

#   def add_room(self, room):
#     self.room = room
#     self.rooms_list.append(self.room) 

#   def get_total_area(self):
#       return sum(room.area for room in self.rooms_list)

# class Room:
#   def __init__(self, room_type, area):
#     self.room_type = room_type
#     self.area = area

# house = House()
# room1 = Room("bedroom", 500)
# room2 = Room("Bathroom", 300)
# room3 = Room("Living Room", 700)
# house.add_room(room1)
# house.add_room(room2)
# house.add_room(room3)
# total_area = house.get_total_area()
# print(total_area)


# 3.
# class Parent:
#   def introduce(self):
#     return "I am Parent."


# class Child1(Parent):
#   def introduce(self):
#     return "I am Child 1."

# class Child2(Parent):
#   def introduce(self):
#     return "I am Child 2"


# class GrandChild(Child1, Child2):
#   pass

# gc = GrandChild()

# intro = gc.introduce()
# print(intro)
# print([cls.__name__ for cls in GrandChild.mro()])



# 4. 
# class Employee:
#   def __init__(self, salary):
#     self.salary = salary

#   @property
#   def salary(self):
#     return self.salary
  
#   @salary.setter
#   def set_salary(self, update_salary):
#     if self.salary < 0:
#       return "Salary must be positive."
#     self.salary = update_salary

#   @property
#   def bonus(self):
#       if self._salary is not None:
#         return self._salary * 0.10
#       return 0

# 7
class Config:
  _instance = None

  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(Config, cls).__new__(cls)
      cls._instance.settings = {}
    return cls._instance
  
  def get_setting(self, key):
    return self.settings.get(key)

  def set_setting(self, key, value):
    self.settings[key] = value

i = Config()
k = Config()

i.set_setting("H", "I")
k.set_setting("M", "A")
print(k.get_setting("H"))
print(i.get_setting("M"))

print("Instance is same? ", i is k)
print("One: ", i.settings)
print("Two: ", k.settings)
