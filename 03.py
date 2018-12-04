# Largest Prime Factor
# n = 600851475143
# factors = []
# primes = []
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         factors.append(i)
# for f in factors:
#     for j in range(2, f // 2 + 1):
#         if f % j == 0:
#             break
#     else:
#         primes.append(f)
# print(factors)
# print(primes)
# print(max(primes))

n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
