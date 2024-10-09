class Node:
  def calculate(self):
    raise NotImplementedError


class Integer(Node):
  def __init__(self, value):
    self.value = value

  def calculate(self):
    return self.value


class Add(Node):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def calculate(self):
    return (
      self.left.calculate() +
      self.right.calculate()
    )


class Multiply(Node):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def calculate(self):
    return (
      self.left.calculate() *
      self.right.calculate()
    )


tree = Multiply(
  Add(Integer(3), Integer(5)),
  Add(Integer(4), Integer(7)),
)


assert tree.calculate() == 88
