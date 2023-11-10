with open('24.txt', 'r') as file:
    line = file.readline().strip()
    lines = line.replace('XZZY', 'XZZ ZZY').split()

print(max([*map(len, lines)]))
