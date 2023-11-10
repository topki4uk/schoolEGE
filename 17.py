with open('17.txt', 'r') as file:
    data = [*map(int, file.readlines())]

evens = [*filter(lambda x: x % 2 == 0, data)]
mean = sum(evens) / len(evens)

count = 0
best = 0
for i in range(len(data)-1):
    n1 = data[i]
    n2 = data[i+1]

    if (n1 % 3 == 0) or (n2 % 3 == 0):
        if (n1 < mean) or (n2 < mean):
            count += 1
            best = max(best, n1+n2)

print(count, best)
