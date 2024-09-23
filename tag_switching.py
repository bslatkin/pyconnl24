
RECTANGLE = object()


def rectangle_init(height, width):
    return (RECTANGLE, height, width)


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
    else:
        raise RuntimeError


def perimeter(obj):
    tag = obj[0]  # how do you verify it's got length?
    if tag == RECTANGLE:      # how do you verify the type is valid?
        return rectangle_perimeter(obj)
    else:
        raise RuntimeError


r1 = rectangle_init(10, 4)
print(area(r1))
print(perimeter(r1))


# how do you update the rectangle properties?
# how do you get the rectangle properties?
# kind of a pain, need to define getters and setters for each one to traverse the tuple and map names to positions
