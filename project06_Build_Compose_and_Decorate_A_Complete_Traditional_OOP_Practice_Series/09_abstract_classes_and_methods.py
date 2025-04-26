from abc import ABC, abstractmethod

class Shape(ABC):
  @classmethod
  @abstractmethod
  def area(self):
    pass

class Rectangle(Shape):
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def area(self):
    print(f"Area of rectangle: {self.height * self.width}")
    
rectangle1 = Rectangle(6, 4)
rectangle1.area()
  