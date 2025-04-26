class Logger:
  def __init__(self, name):
    self.name = name
    print(f"Object {self.name} is created. \n")

  def __del__(self):
    print(f"Object {self.name} is destroyed. \n")


# Prints Object is created with each names.
Object1 = Logger("Adam")
Object2 = Logger("Chris")

# Automatically prints Object is destroyed with each names. (Timing depends on the garbage collector.)
del Object2
del Object1