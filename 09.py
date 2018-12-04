# Special Pythagorean triplet
a = 0
b = 0
c = 0
for i in range(1, 500):
    c = i
    if b < c:
        for j in range(1, 500):
            b = j
            if a < b:
                for k in range(1, 500):
                    a = k
                    if a**2 + b**2 is c**2:
                        print(a, b, c)
