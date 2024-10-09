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


