def f(n, v):
    if n > 12:
        return 0

    if n == 12 and v:
        return 1

    if n == 10:
        v = True

    return f(n+1, v) + f(n+2, v) + f(2*n, v)


print(f(3, False))
