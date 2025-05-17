from functools import singledispatch
import math


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


# Traversing the structure
@singledispatch
def traverse(node, algebra):
    raise NotImplementedError(node)


@traverse.register(Integer)
def trav_value(node, algebra):
    return algebra(node, node.value)


@traverse.register(Add)
@traverse.register(Multiply)
def tav_binop(node, algebra):
    left_value = traverse(node.left, algebra)
    right_value = traverse(node.right, algebra)
    return algebra(node, left_value, right_value)


# Applying an algebra
@singledispatch
def arithmetic(node, *values):
    raise NotImplementedError(node, values)


@arithmetic.register(Integer)
def arithmetic_value(_, value):
    return value


@arithmetic.register(Add)
def arithmetic_add(_, left, right):
    return left + right


@arithmetic.register(Multiply)
def arithmetic_multiply(_, left, right):
    return left * right


tree = Multiply(
    Add(
        Integer(2),
        Integer(3),
    ),
    Integer(4),
)


assert traverse(tree, arithmetic) == 20


class Power:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent


@traverse.register(Power)
def trav_power(node, algebra):
    base_value = traverse(node.base, algebra)
    exponent_value = traverse(node.exponent, algebra)
    return algebra(node, base_value, exponent_value)


@arithmetic.register(Power)
def arithmetic_power(_, base, exponent):
    return base**exponent


tree2 = Add(
    Power(
        Integer(2),
        Integer(3),
    ),
    Integer(4),
)


assert traverse(tree2, arithmetic) == 12


class PositiveInteger(Integer):
    def __init__(self, value):
        assert value > 0
        super().__init__(value)


tree3 = Add(PositiveInteger(3), Integer(-1))


assert traverse(tree3, arithmetic) == 2


# Defining an algebra for pretty printing
@singledispatch
def pretty_algebra(node, *values):
    raise NotImplementedError(node, values)


@pretty_algebra.register(Integer)
def pretty_int(_, value):
    return str(value)


@pretty_algebra.register(Add)
def pretty_add(_, left, right):
    return f"{left} + {right}"


@pretty_algebra.register(Multiply)
def pretty_multiply(_, left, right):
    return f"{left} * {right}"


@pretty_algebra.register(Power)
def pretty_power(_, left, right):
    return f"{left}^{right}"


# Examples
print(traverse(tree, pretty_algebra))
print(traverse(tree2, pretty_algebra))
print(traverse(tree3, pretty_algebra))


# Another algebra
@singledispatch
def complexity_algebra(node, *values):
    raise NotImplementedError


@complexity_algebra.register(Integer)
def complexity_int(_, value):
    return 0


@complexity_algebra.register(Add)
def complexity_add(_, left, right):
    return 1 + left + right


@complexity_algebra.register(Multiply)
def complexity_mul(_, left, right):
    return 2 + left + right


@complexity_algebra.register(Power)
def complexity_pow(_, base, exp):
    return 4 + base + exp


print(traverse(tree, complexity_algebra))
print(traverse(tree2, complexity_algebra))
print(traverse(tree3, complexity_algebra))
