class Multiplier:
  def __init__(self, factor):
    self.factor = factor

  def __call__(self, value):
    return value * self.factor

  
multiply = Multiplier(8)
print(callable(multiply))
result = multiply(5)
print(result)