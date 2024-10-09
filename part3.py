from functools import singledispatch

@singledispatch
def my_print(value):
  print(f"Unexpected: {type(value)}, {value!r}")

@my_print.register(int)
def _(value):
  print("Integer!", value)

@my_print.register(float)
def _(value):
  print("Float!", value)


my_print(10)
my_print(1.23)
my_print("hello")


@singledispatch
def calculate(node):
    raise NotImplementedError


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


@calculate.register(Integer)
def _(node):
    return node.value


@calculate.register(Add)
def _(node):
  return calculate(node.left) + calculate(node.right)


@calculate.register(Multiply)
def _(node):
  return calculate(node.left) * calculate(node.right)



tree = Multiply(
  Add(
    Integer(2),
    Integer(3),
  ),
  Integer(4),
)


assert calculate(tree) == 20


class Power:
  def __init__(self, base, exponent):
    self.base = base
    self.exponent = exponent


@calculate.register(Power)
def _(node):
  return (
    calculate(node.base) **
    calculate(node.exponent)
  )


tree2 = Add(
  Power(
    Integer(2),
    Integer(3),
  ),
  Integer(4),
)


assert calculate(tree2) == 12


class PositiveInteger(Integer):
  def __init__(self, value):
    assert value > 0
    super().__init__(value)


tree3 = Add(PositiveInteger(3), Integer(-1))
assert calculate(tree3) == 2


@singledispatch
def pretty(node):
  raise NotImplementedError

@pretty.register(Integer)
def _(node):
  return f"{node.value}"

@pretty.register(Add)
def _(node):
  return (
    f"({pretty(node.left)} +"
    f" {pretty(node.right)})"
  )

@pretty.register(Multiply)
def _(node):
  return (
    f"({pretty(node.left)} *"
    f" {pretty(node.right)})"
  )

@pretty.register(Power)
def _(node):
  return (
    f"({pretty(node.base)} ^"
    f" {pretty(node.exponent)})"
  )



tree4 = Multiply(
  Integer(2),
  Power(
    Integer(10),
    Add(Integer(3), Integer(4)),
  )
)

print(pretty(tree4))
assert pretty(tree4) == "(2 * (10 ^ (3 + 4)))"

