def f(n):
    bin_n = bin(n)[2:]

    bin_n = bin_n[1:]

    if '1' not in bin_n:
        return 0

    while bin_n[0] == '0':
        bin_n = bin_n[1:]

    return n - int(bin_n, 2)


ss = set()

for i in range(10, 1001):
    r = f(i)
    ss.add(r)

print(ss)
