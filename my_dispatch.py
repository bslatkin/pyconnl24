from collections import defaultdict


dispatch_map = defaultdict(dict)


def register_dispatch(dispatch_func, kind, func):
  kind_map = dispatch_map[dispatch_func]
  kind_map[kind] = func


def call_dispatch(dispatch_func, value, *args, **kwargs):
  kind_map = dispatch_map[dispatch_func]
  for kind in type(value).__mro__:
    if kind in kind_map:
      func = kind_map[kind]
      return func(value, *args, **kwargs)
  return dispatch_func(value, *args, **kwargs)



from functools import wraps

def my_dispatch(dispatch_func):
  @wraps(dispatch_func)
  def inner(*args, **kwargs):
    return call_dispatch(dispatch_func, *args, **kwargs)

  setattr(inner, "register", register_helper(dispatch_func))
  return inner


def register_helper(dispatch_func):
  def outer(kind):
    def decorator(func):
      register_dispatch(dispatch_func, kind, func)
      return func

    return decorator

  return outer




@my_dispatch
def my_print(value):
  print(f"Default implementation: {value}")

@my_print.register(int)
def _(value):
  print(f"Integer print: {value}")

@my_print.register(float)
def _(value):
  print(f"Float print: {value}")


my_print(5)
my_print(1.23)
my_print("unknown")
