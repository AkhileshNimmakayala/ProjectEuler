# Highly divisible triangular number
import os

def trianglenumber(i):
    n = int(i * (i + 1) / 2)
    return n


def factors(f):
    counter = 1
    for i in range(1, f + 1):
        if f % i == 0:
            counter += 1

    return counter

def numberofdivisors(lim):
    start = 1
    z = True
    while z is True:
        for i in range(start, start + 1 + 1):
            x = trianglenumber(i)
            if factors(x) > lim:
                print(x)
                z = False
                os.system('say "Program terminated"')
                break
            max += 1

# Begin with start = 1 for lim = 100 then use position() to find next start value
# and update start = position(n) and update lim = 200 and so on until lim = 500
# lim - position - triangle num
# 100 - 385      - 73920
# 200 - 2015     - 2031120
# 300 - 2079     - 2162160
# 400 - 5984     - 17907120
# 500 - 12375    - 76576500
numberofdivisors(100)

def position(n):
    i = (((8*n+1)**0.5)-1)/2
    print(i)

position(76576500)