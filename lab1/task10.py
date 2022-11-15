nums = []
for i in range(3):
    n = int(input())
    nums.append(n)

nums.sort()

result = ""
for n in nums:
    result += str(n) + " "
print(result)