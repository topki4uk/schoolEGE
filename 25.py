def f(n):
    dels = []

    if n**0.5 != int(n**0.5):
        return False

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if i % 2 != 0:
                dels.append(i)

            if (n // i) % 2 != 0:
                dels.append(n // i)

    if len(set(dels)) == 5:
        return True

    return False


for i in range(45_000_000, 50_000_001):
    if f(i):
        print(i)
