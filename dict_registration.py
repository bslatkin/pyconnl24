
RECTANGLE = object()

def rectangle_area(obj):
    return obj["height"] * obj["width"]


def rectangle_perimeter(obj):
    return 2 * (obj["height"] + obj["width"])


# Just put the methods to call inside the object

def rectangle_init(height, width):
    return {
        "type": RECTANGLE,
        "height": height,
        "width": width,
        "area": rectangle_area,
        "perimeter": rectangle_perimeter,
    }



# Now the functions to do actions just look up the methods to call and then call them with the object.
# This solves the recursive dependency problem


r1 = rectangle_init(6, 7)
print(r1["area"](r1))

# Bad: Repetative having to refer to the object twice


# You can delcare functions to route appropriately, which is quite a bit of boiler plate.


def area(obj):
    return obj["area"](obj)


r1 = rectangle_init(6, 7)
print(area(r1))


def perimeter(obj):
    return obj["perimeter"](obj)


print(perimeter(r1))


# How does superclass delegation work?

# Just point to the parent type methods when you create the object


SOLID_RECTANGLE = object()

def solid_rectangle_init(color, height, width):
    return {
        "type": SOLID_RECTANGLE,
        "color": color,
        "height": height,
        "width": width,
        "area": rectangle_area,
        "perimeter": rectangle_perimeter,
    }

r2 = solid_rectangle_init("red", 3, 4)
print(area(r2))
