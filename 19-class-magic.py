# https://docs.python.org/3/reference/datamodel.html

class Example:

  def __init__(self, v):
    self.v = v

  def __add__(self, other):
    return self.v + other.v

  def __lt__(self, other):
    return self.v < other.v

x = Example(5)
y = Example(6)

print(x + y)
print(x < y)