
RECTANGLE = object()


def rectangle_init(height, width):
    return (RECTANGLE, height, width)


# kind of a pain, need to define getters and setters for each one to traverse the tuple and map names to positions

def rectangle_height(obj):
    assert obj[0] == RECTANGLE
    return obj[1]


def rectangle_width(obj):
    assert obj[0] == RECTANGLE
    return obj[2]


def rectangle_area(obj):
    _, height, width = obj
    return height * width


def rectangle_perimeter(obj):
    _, height, width = obj
    return 2 * (height + width)


def area(obj):
    tag = obj[0]  # how do you verify it's got length?
    if tag == RECTANGLE:      # how do you verify the type is valid?
        return rectangle_area(obj)
    # TODO: Put other types in here
    else:
        raise RuntimeError


r1 = rectangle_init(10, 4)
print(area(r1))


def perimeter(obj):
    tag = obj[0]  # how do you verify it's got length?
    if tag == RECTANGLE:      # how do you verify the type is valid?
        return rectangle_perimeter(obj)
    else:
        raise RuntimeError


print(perimeter(r1))



# how do you update the rectangle properties? you can only do this with immutable updates

def rectangle_set_width(obj, new_width):
    return (RECTANGLE, obj[1], new_width)


def rectangle_set_height(obj, new_height):
    return (RECTANGLE, new_height, obj[2])


def rectangle_update(obj, height=None, width=None):
    _, new_height, new_width = obj
    if height is not None:
        new_height = height
    if width is not None:
        new_width = width

    return (RECTANGLE, new_height, new_width)

