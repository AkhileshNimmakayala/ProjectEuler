# Large sum
nums = []
result = 0
with open("/Users/AkhileshNimmakayala/Downloads/test", "r") as file:
    for line in file:
        nums.append(int(line))
for num in nums:
    result += num
print(result)
count = 0
for i in str(result):
    if count < 10:
        print(i, end=' ')
        count += 1
