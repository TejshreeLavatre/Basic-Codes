a, b = 0, 1


def fib():
    global a, b
    while True:
        a, b = b, a + b
        yield a


f = fib()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
print(f.__next__())
