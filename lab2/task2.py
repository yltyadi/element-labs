n = int(input())

smallest = n
for i in range(2, n + 1):
    if (n % i == 0):
        if i < smallest:
            smallest = i
print(smallest)