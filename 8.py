from itertools import *

p = [*permutations('МАТВЕЙ')]
count = 0

for sub in p:
    word = ''.join(sub)
    if word[0] != 'Й':
        if 'АЕ' not in word:
            count += 1

print(count)
