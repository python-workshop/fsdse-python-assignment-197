def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    result = 0 + a
    for i in range(1, b):
        result += a
    return result


def subtract(a, b):
    b = -b
    return a + b