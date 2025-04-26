class Product:
  
  def __init__(self, price):
    self.__price = price

  @property
  def price(self):
    return self.__price
  
  @price.setter
  def price(self, price):
    self.__price = price
  
  @price.deleter
  def price(self):
    del self.__price


p = Product(100)
print(p.price)     # 100

p.price = 150
print(p.price)     # 150

del p.price 
# print(p.price)  # Throws an attribute error after deletion.    
