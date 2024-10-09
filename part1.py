class Integer:
  def __init__(self, value):
    self.value = value


class Add:
  def __init__(self, left, right):
    self.left = left
    self.right = right


class Multiply:
  def __init__(self, left, right):
    self.left = left
    self.right = right


tree = Multiply(
  Add(Integer(3), Integer(5)),
  Add(Integer(4), Integer(7)),
)


def calculate(node):
  if isinstance(node, Integer):
    return node.value
  elif isinstance(node, Add):
    return calculate(node.left) + calculate(node.right)
  elif isinstance(node, Multiply):
    return calculate(node.left) * calculate(node.right)
  else:
    raise NotImplementedError


assert calculate(tree) == 88


class Power:
  def __init__(self, base, exponent):
    self.base = base
    self.exponent = exponent


def calculate2(node):
  if isinstance(node, Integer):
    return node.value
  elif isinstance(node, Add):
    return calculate2(node.left) + calculate2(node.right)
  elif isinstance(node, Multiply):
    return calculate2(node.left) * calculate2(node.right)
  elif isinstance(node, Power):
    return calculate2(node.base) ** calculate2(node.exponent)
  else:
    raise NotImplementedError


tree2 = Add(
  Power(
    Integer(2),
    Integer(3),
  ),
  Integer(4),
)


assert calculate2(tree2) == 12
