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
        return self.left.calculate() + self.right.calculate()


class Multiply(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calculate(self):
        return self.left.calculate() * self.right.calculate()


tree = Multiply(
    Add(Integer(3), Integer(5)),
    Add(Integer(4), Integer(7)),
)


assert tree.calculate() == 88


class Power(Node):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def calculate(self):
        return self.base.calculate() ** self.exponent.calculate()


tree2 = Add(
    Power(
        Integer(2),
        Integer(3),
    ),
    Integer(4),
)


assert tree2.calculate() == 12


class PositiveInteger(Integer):
    def __init__(self, value):
        assert value > 0
        super().__init__(value)


tree3 = Add(PositiveInteger(3), Integer(-1))
assert tree3.calculate() == 2


class Node2:
    def calculate(self):
        raise NotImplementedError

    def pretty(self):
        raise NotImplementedError


class Integer(Node2):
    def __init__(self, value):
        self.value = value

    def calculate(self):
        return self.value

    def pretty(self):
        return f"{self.value}"


class Add(Node2):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calculate(self):
        return self.left.calculate() + self.right.calculate()

    def pretty(self):
        return f"({self.left.pretty()} +" f" {self.right.pretty()})"


class Multiply(Node2):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def calculate(self):
        return self.left.calculate() * self.right.calculate()

    def pretty(self):
        return f"({self.left.pretty()} *" f" {self.right.pretty()})"


class Power(Node2):
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def calculate(self):
        return self.base.calculate() ** self.exponent.calculate()

    def pretty(self):
        return f"({self.base.pretty()}^{self.exponent.pretty()})"


tree4 = Multiply(
    Integer(2),
    Power(
        Integer(10),
        Add(Integer(3), Integer(4)),
    ),
)

assert tree4.pretty() == "(2 * (10^(3 + 4)))"
