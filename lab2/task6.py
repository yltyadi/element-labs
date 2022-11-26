def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result

a, n = input().split()
print(power(int(a), int(n)))