def fact(n):
    # Calculate n! iteratively
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


for i in range(10):
    print(i, fact(i))
