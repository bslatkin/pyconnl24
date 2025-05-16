from functools import singledispatch
import math


class Value:
    def __init__(self, value):
        self.value = value


class Natural(Value):
    pass


class Whole(Value):
    pass


class Integer(Value):
    pass


class Rational(Value):
    pass


class Irrational(Value):
    pass


class Real(Value):
    pass


class Complex(Value):
    pass


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOp):
    pass


class Subtract(BinaryOp):
    pass


class Multiply(BinaryOp):
    pass


class Divide(BinaryOp):
    pass


class Power(BinaryOp):
    pass


class UnaryOp:
    def __init__(self, parameter):
        self.parameter = parameter


class Negate(UnaryOp):
    pass


class Sqrt(UnaryOp):
    pass


class Abs(UnaryOp):
    pass


# Traversing the structure
@singledispatch
def my_catamorphism(node, algebra):
    raise NotImplementedError(node)


@my_catamorphism.register(Value)
def _(node, algebra):
    return algebra(node, node.value)


@my_catamorphism.register(BinaryOp)
def _(node, algebra):
    left_value = my_catamorphism(node.left, algebra)
    right_value = my_catamorphism(node.right, algebra)
    return algebra(node, left_value, right_value)


@my_catamorphism.register(UnaryOp)
def _(node, algebra):
    value = my_catamorphism(node.parameter, algebra)
    return algebra(node, value)


# Applying an algebra
@singledispatch
def my_algebra(node, *values):
    raise NotImplementedError(node, values)


@my_algebra.register(Value)
def my_value(_, value):
    return value


@my_algebra.register(Add)
def my_add(_, left, right):
    return left + right


@my_algebra.register(Subtract)
def my_subtract(_, left, right):
    return left - right


@my_algebra.register(Multiply)
def my_multiply(_, left, right):
    return left * right


@my_algebra.register(Divide)
def my_divide(_, left, right):
    return left / right


@my_algebra.register(Power)
def my_power(_, left, right):
    return math.pow(left, right)


@my_algebra.register(Negate)
def my_negate(_, value):
    return -value


@my_algebra.register(Sqrt)
def my_sqrt(_, value):
    return math.sqrt(value)


@my_algebra.register(Abs)
def my_abs(_, value):
    if value >= 0:
        return value
    else:
        return -value


# Example 1
tree = Multiply(
    Add(Integer(3), Integer(5)),
    Add(Integer(4), Integer(7)),
)

print(my_catamorphism(tree, my_algebra))


# Example 2
tree2 = Add(
    Power(
        Integer(2),
        Integer(3),
    ),
    Integer(4),
)

print(my_catamorphism(tree2, my_algebra))

# Example 3
tree3 = Subtract(
    Add(
        Sqrt(
            Integer(2),
        ),
        Integer(4),
    ),
    Abs(Integer(-3)),
)

print(my_catamorphism(tree3, my_algebra))


# Defining an algebra for pretty printing
@singledispatch
def pretty_algebra(node, *values):
    raise NotImplementedError(node, values)


@pretty_algebra.register(Value)
def pretty_value(_, value):
    return str(value)


@pretty_algebra.register(Add)
def pretty_add(_, left, right):
    return f"{left} + {right}"


@pretty_algebra.register(Subtract)
def pretty_subtract(_, left, right):
    return f"{left} - {right}"


@pretty_algebra.register(Multiply)
def pretty_multiply(_, left, right):
    return f"{left} * {right}"


@pretty_algebra.register(Divide)
def pretty_divide(_, left, right):
    return f"{left} / {right}"


@pretty_algebra.register(Power)
def pretty_power(_, left, right):
    return f"{left} ^ {right}"


@pretty_algebra.register(Negate)
def pretty_negate(_, value):
    return f"-{value}"


@pretty_algebra.register(Sqrt)
def pretty_sqrt(_, value):
    return f"⎷{value}"


@pretty_algebra.register(Abs)
def pretty_abs(_, value):
    return f"|{value}|"


# Examples
print(my_catamorphism(tree, pretty_algebra))
print(my_catamorphism(tree2, pretty_algebra))
print(my_catamorphism(tree3, pretty_algebra))
