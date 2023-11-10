with open('9.csv', 'r') as file:
    data = []

    for line in file.readlines():
        data += [*map(float, line.replace(',', '.').split(';'))]

count = 0
for i in range(len(data)-1):
    n1 = data[i]
    n2 = data[i+1]
    delta = n2 - n1

    if n2 - n1 <= -2:
        count += 1

print(count)
