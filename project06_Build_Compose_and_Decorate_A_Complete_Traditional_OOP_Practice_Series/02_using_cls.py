class Counter:
  count = 0
  def __init__(self, word):
    self.name = word
    Counter.count += 1

  @classmethod
  def count_objects(cls):
    print(f"Total objects created: {cls.count}.")
    
count1 = Counter("hello")
count2 = Counter("bye")
count3 = Counter("see ya")

Counter.count_objects()