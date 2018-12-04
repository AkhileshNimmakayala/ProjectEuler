# 10001st prime
primes = []
n = 2
while len(primes) != 10001:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            n += 1
            break
    else:
        primes.append(n)
        n += 1
print(primes[10000])
