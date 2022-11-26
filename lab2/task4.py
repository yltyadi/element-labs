n = int(input())

nums = []
for i in range(n):
    a = int(input())
    nums.append(a)

sum = 0
for n in nums:
    sum += n

print(sum)