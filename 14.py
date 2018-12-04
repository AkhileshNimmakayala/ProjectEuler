# Longest Collatz sequence
lim = int(input("Enter the number: "))
maxseq = 0
result = 0
for n in range(1, lim + 1):
    current = n
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            seq.append(n)
        else:
            n = 3 * n + 1
            seq.append(n)
    terms = len(seq)
    print(seq)
    if terms > maxseq:
        maxseq = terms
        result = current
    seq.clear()
print(result)


