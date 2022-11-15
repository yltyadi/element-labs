nums = []
for i in range(3):
    n = int(input())
    nums.append(n)

high = 0
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    if count > high:
        high = count

if high == 1:
    high -= 1
print(high)