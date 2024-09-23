def rectangle_init(height, width):
    obj = {
        "height": height,
        "width": width,
    }

    def area():
        return obj["height"] * obj["width"]

    def perimeter():
        return 2 * (obj["height"] + obj["width"])

    obj["area"] = area
    obj["perimeter"] = perimeter

    return obj


r1 = rectangle_init(10, 4)
print(r1["area"]())
print(r1["perimeter"]())

r1["height"] = 8
print(r1["area"]())
print(r1["perimeter"]())


def square_init(
