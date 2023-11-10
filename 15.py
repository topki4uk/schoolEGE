length = 0

for a in range(-100, 101):
    for b in range(a, 101):
        flag = True

        for x in range(-100, 101):
            f = ((a <= x <= b) <= (x**2 <= 100)) and ((x**2 <= 64) <= (a <= x <= b))

            if not f:
                flag = False
                break

        if flag:
            length = max(length, b-a)

print(length)
