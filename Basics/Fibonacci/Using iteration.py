def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


print(fib(0), fib(1), fib(2), fib(3),
fib(4),
fib(5),
fib(6),
fib(7))
