class A:
  def show(self):
    print("I am A.")

class B(A):
  def show(self):
    print("I am B.")

class C(A):
  def show(self):
    print("I am C.")

class D(B, C):
    pass

d = D()
d.show()

print(D.__mro__)