def first(n, m):
    return (second(n+1, m) and second(n, m+1) and second(n*2, m) and second(n, 3*m)) and not second(n, m)


def second(n, m):
    return (n+1 + m >= 69) or (n*2 + m >= 69) or (n + 3*m >= 69)


for i in range(1, 59):
    if first(10, i):
        print(i)
