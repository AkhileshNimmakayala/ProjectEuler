# Largest palindrome product
Palindromes = []
d2 = 100
while d2 in range(100,1000):
    for d1 in range(100, 1000):
        product = d1 * d2
        reverse = str(product)[::-1]
        if str(product) == reverse:
            Palindromes.append(product)
    else:
        d2 += 1
print(max(Palindromes))
print(d1, d2)
