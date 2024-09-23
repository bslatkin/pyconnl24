
RECTANGLE = object()


def rectangle_init(height, width):
    return {
        "type": RECTANGLE,
        "height": height,
        "width": width,
    }

# Better: Don't need the accessors because we can just look in the dict

def rectangle_area(obj):
    return obj["height"] * obj["width"]


def rectangle_perimeter(obj):
    return 2 * (obj["height"] + obj["width"])


def area(obj):
    obj_type = obj["type"]  # how do you verify it's got length?
    if obj_type == RECTANGLE:      # how do you verify the type is valid?
        return rectangle_area(obj)
    # TODO: Put other types in here
    else:
        raise RuntimeError


r1 = rectangle_init(6, 7)
print(area(r1))


def perimeter(obj):
    obj_type = obj["type"]  # how do you verify it's got length?
    if obj_type == RECTANGLE:      # how do you verify the type is valid?
        return rectangle_perimeter(obj)
    else:
        raise RuntimeError


print(perimeter(r1))


# Better: Possible to update parameters by poking attributes in the dictionary
# this looks more like an object with encapsulated, mutable state

r1["height"] = 9
print(area(r1))
print(perimeter(r1))

# Problems:
# - Still need to modify "area" and "perimeter" functions each time a new type is added to the system
# - Users can modify the "type" key/value in the object dictionary
# - No ability to delegate methods to a super class


# Trying to add polymorphism

SOLID_RECTANGLE = object()

def solid_rectangle_init(color, height, width):
    return {
        "type": SOLID_RECTANGLE,
        "color": color,
        "height": height,
        "width": width,
    }


def area(obj):
    obj_type = obj["type"]
    if obj_type in (RECTANGLE, SOLID_RECTANGLE):
        return rectangle_area(obj)
    else:
        raise RuntimeError


r2 = solid_rectangle_init('red', 3, 4)
print(area(r2))


def perimeter(obj):
    obj_type = obj["type"]
    if obj_type in (RECTANGLE, SOLID_RECTANGLE):
        return rectangle_perimeter(obj)
    else:
        raise RuntimeError

print(perimeter(r2))

# Bad:
# You manually have to do this super class delegation in each method
# Each function needs full knowledge of every type of object in the program that will ever statisfy the interface, which makes it extremely difficult to make your code modular; you end up getting coupling where the most common object methods have to import and depend on every other module in the whole codebase -- show a diagram of this dependency hell, it's kind of a recursive dependency too; the bottom of the hierarchy that defines area() is what needs to be called by all code that consumes these objects; but that bottom part of the hierarchy also needs to depend on each of the modules



