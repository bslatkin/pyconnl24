
RECTANGLE = object()

def rectangle_area(obj):
    return obj["height"] * obj["width"]


def rectangle_perimeter(obj):
    return 2 * (obj["height"] + obj["width"])


# Put methods in the object but also create a closure over them so you don't need to pass them in as the first parameter
# This complicates the constructor because you have to do it in two phases so the methods can refer back to the object that is just being allocated

def rectangle_init(height, width):
    obj = {
        "type": RECTANGLE,
        "height": height,
        "width": width,
    }
    obj["area"] = lambda: rectangle_area(obj)
    obj["perimeter"] = lambda: rectangle_perimeter(obj)
    return obj



# Now you can just do the lookups and make the call, only referring to the object variable name once


r1 = rectangle_init(6, 7)
print(r1["area"]())
print(r1["perimeter"]())



# Bad: Super class delegation has to repeat the process of creating the closures using lambda, lots of boiler plate here when the only thing that really needed to be added was the "color" attribute assignment


SOLID_RECTANGLE = object()

def solid_rectangle_init(color, height, width):
    obj = {
        "type": SOLID_RECTANGLE,
        "color": color,
        "height": height,
        "width": width,
    }
    obj["area"] = lambda: rectangle_area(obj)
    obj["perimeter"] = lambda: rectangle_perimeter(obj)
    return obj

r2 = solid_rectangle_init("red", 3, 4)
print(r2["area"]())
print(r2["perimeter"]())


# We can try to reduce this boiler plate in init() by reusing the parent class's implementation of init, breaking it into pieces

def solid_rectangle_init(color, height, width):
    obj = {
        "type": SOLID_RECTANGLE,
        "color": color,
        "height": height,
        "width": width,
    }
    obj["area"] = lambda: rectangle_area(obj)
    obj["perimeter"] = lambda: rectangle_perimeter(obj)
    return obj

r3 = solid_rectangle_init("red", 3, 4)
print(r3["area"]())
print(r3["perimeter"]())



# TODO: Add modifications to the object here to show that the closure works

