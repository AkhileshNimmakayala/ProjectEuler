# Even Fibonacci Numbers
seq = [1]
n = 1
last = 0
while n < 4000000:
    last = max(seq)
    seq.append(last + n)
    n = last
print(seq)
Total = 0
for i in seq:
    if i % 2 == 0:
        Total += i
print(Total)
