print('w x y z f')

for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = ((x <= y) == (z <= w)) or (x and w)

                if not f:
                    print(w, x, y, z, int(f))
