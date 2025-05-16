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

print("Arithmetic")
print("tree: ", my_catamorphism(tree, my_algebra))


# Example 2
tree2 = Add(
    Power(
        Integer(2),
        Integer(3),
    ),
    Integer(4),
)

print("tree2:", my_catamorphism(tree2, my_algebra))

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

print("tree3:", my_catamorphism(tree3, my_algebra))


# Example 4
tree4 = Subtract(
    Integer(4),
    Complex(2 - 3j),
)

print("tree4:", my_catamorphism(tree4, my_algebra))


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
print("Pretty printing")
print("tree: ", my_catamorphism(tree, pretty_algebra))
print("tree2:", my_catamorphism(tree2, pretty_algebra))
print("tree3:", my_catamorphism(tree3, pretty_algebra))
print("tree4:", my_catamorphism(tree4, pretty_algebra))


# Type checker
@singledispatch
def type_check_algebra(node, *values):
    raise NotImplementedError(node, values)


@type_check_algebra.register(Value)
def type_check_value(node, _):
    if isinstance(node, (Natural, Whole, Integer, Rational)):
        return Rational
    elif isinstance(node, (Complex,)):
        return Complex
    else:
        return Irrational


@type_check_algebra.register(Add)
@type_check_algebra.register(Subtract)
@type_check_algebra.register(Multiply)
@type_check_algebra.register(Divide)
@type_check_algebra.register(Power)
def type_check_most_constraint(_, left, right):
    if Complex in (left, right):
        return Complex
    elif Irrational in (left, right):
        return Irrational
    else:
        return Rational


@type_check_algebra.register(Negate)
@type_check_algebra.register(Abs)
def type_check_passthrough(_, value):
    return value


@type_check_algebra.register(Sqrt)
def type_check_sqrt(_, value):
    return Irrational


# Examples
print("Type check")
print("tree: ", my_catamorphism(tree, type_check_algebra))
print("tree2:", my_catamorphism(tree2, type_check_algebra))
print("tree3:", my_catamorphism(tree3, type_check_algebra))
print("tree4:", my_catamorphism(tree4, type_check_algebra))


# Complexity/Size Analysis
@singledispatch
def complexity_algebra(node, *values):
    raise NotImplementedError(node, values)


@complexity_algebra.register(Value)
def complexity_value(_, value):
    return 0


@complexity_algebra.register(Complex)
def complexity_value(_, value):
    return 2


@complexity_algebra.register(Add)
def complexity_add(_, left, right):
    return 1 + left + right


@complexity_algebra.register(Subtract)
def complexity_subtract(_, left, right):
    return 1 + left + right


@complexity_algebra.register(Multiply)
def complexity_multiply(_, left, right):
    return 4 + left + right


@complexity_algebra.register(Divide)
def complexity_divide(_, left, right):
    return 8 + left + right


@complexity_algebra.register(Power)
def complexity_power(_, left, right):
    return 16 + left + right


@complexity_algebra.register(Negate)
def complexity_negate(_, value):
    return 1 + value


@complexity_algebra.register(Sqrt)
def complexity_sqrt(_, value):
    return 16 + value


@complexity_algebra.register(Abs)
def complexity_abs(_, value):
    return 2 + value


# Examples
print("Complexity")
print("tree: ", my_catamorphism(tree, complexity_algebra))
print("tree2:", my_catamorphism(tree2, complexity_algebra))
print("tree3:", my_catamorphism(tree3, complexity_algebra))
print("tree4:", my_catamorphism(tree4, complexity_algebra))
