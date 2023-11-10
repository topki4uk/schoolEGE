def first(n, m):
    return (second(n+1, m) or second(n, m+1) or second(n*2, m) or second(n, 3*m)) and not third(n, m)


def second(n, m):
    return (third(n+1, m) and third(n, m+1) and third(n*2, m) and third(n, 3*m)) and not third(n, m)


def third(n, m):
    return (n+1 + m >= 69) or (n*2 + m >= 69) or (n + 3*m >= 69)


for i in range(1, 59):
    if first(10, i):
        print(i)
