class Car:
  def __init__(self, brand):
    self.brand = brand

  def start(self):
    print(f"{self.brand} has started.")


Mustang = Car("Mustang")

print(Mustang.brand)
Mustang.start()