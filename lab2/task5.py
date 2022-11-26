binary = input()

result = 0
for i in range(len(binary)):
    if int(binary[i]) == 1:
        result += 2**(len(binary) - i - 1)
print(result)