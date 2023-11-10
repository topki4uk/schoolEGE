from itertools import combinations


with open('26.txt', 'r') as file:
    N = int(file.readline())
    data = set(map(int, file.readlines()))

combos = [*combinations(data, r=2)]
count = 0
best = 0

for combo in combos:
    n1 = combo[0]
    n2 = combo[1]

    if n1 % 2 != 0 and n2 % 2 != 0:
        mean = (n1 + n2) // 2

        if mean in data:
            count += 1
            best = max(best, mean)

print(count, best)
