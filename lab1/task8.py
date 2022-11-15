a = int(input())
b = int(input())
c = int(input())

if (a > b and a > c):
    if a < (b + c):
        print("YES")
    else:
        print("NO")
elif (b > a and b > c):
    if b < (a + c):
        print("YES")
    else:
        print("NO")
elif (c > a and c > b):
    if c < (a + b):
        print("YES")
    else:
        print("NO")