
def calculation(a, b):
    yield a + b
    yield a - b


x = calculation(3, 7)
print(*x)
print(*calculation(6, 7))
