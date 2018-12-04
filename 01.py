# Multiples of 3 and 5
# Using while()
n = 999
i = j = k = sum3 = sum5 = sum15 = 0
while 3 * i <= n:
    sum3 += 3 * i
    i += 1
while 5 * j <= n:
    sum5 += 5 * j
    j += 1
while 15 * k <= n:
    sum15 += 15 * k
    k += 1
print(sum3 + sum5 - sum15)

# Using if()
m = 999
sums = 0
for i in range(1, m+1):
    if i % 3 == 0:
        sums += i
    elif i % 5 == 0:
        sums += i
    elif i % 15 == 0:
        sums -= i
print(sums)

# Using for()
limit = 999
result = 0
for i in range(1, 999 + 1):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)

# Using list comprehension
k = 999
q = sum([x for x in range(1, k + 1) if x % 3 == 0 or x % 5 == 0])
print(q)

# Using Mathematics... Damn! efficient for huge limit
lim = 999
total = 0
a = lim//3  # To get max divisor of limit with 3
sums3 = 3 * (a*(a+1)/2)  # Sum of 'n' natural no.s is n(n+1)/2
b = lim//5
sums5 = 5 * (b*(b+1)/2)
c = lim//15
sums15 = 15 * (c*(c+1)/2)
Total = sums3 + sums5 - sums15
print(Total)
# Can also be done using Arithmetic Progression
