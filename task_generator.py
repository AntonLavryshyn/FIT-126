import random

n = 3
m = 9
sect = 0

variants = [[0] * n for i in range(m)]

for i in variants:
    sect += 1
    for j in i:
        if sect == 1 or 2 or 5 or 6 and sect < 8:
            j = random.randint(1, 3)
        if sect == 3 or 6:
            j = random.randint(1, 5)
        if sect == 4:
            j = random.randint(1, 4)
        if sect == 8:
            j = random.randint(1, 30)
        if sect == 9:
            j = random.randint(1, 6)
    print('Selection', sect, ': ', j)














