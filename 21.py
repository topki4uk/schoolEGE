def first(n, m):
    return (second(n+1, m) and second(n, m+1) and second(n*2, m) and second(n, 3*m)) and not fourth(n, m)


def second(n, m):
    return (third(n+1, m) or third(n, m+1) or third(n*2, m) or third(n, 3*m)) or fourth(n, m)


def third(n, m):
    return (fourth(n+1, m) and fourth(n, m+1) and fourth(n*2, m) and fourth(n, 3*m)) and not fourth(n, m)


def fourth(n, m):
    return (n + 1 + m >= 69) or (n * 2 + m >= 69) or (n + 3 * m >= 69)


for i in range(1, 59):
    if first(10, i):
        print(i)
