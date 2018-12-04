# Summation of primes
num = int(input("enter a number: "))
primes = [2]
n = 2
for n in range(3, num, 2):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            break
    else:
        primes.append(n)
        print(n)
print(sum(primes))
