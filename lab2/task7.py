n = list(map(int, input().split()))

oneCount = 0
zeroCount = 0
for i in n:
    if i == 1:
        oneCount += 1
    if i == 0:
        zeroCount += 1

if (oneCount > zeroCount):
    print(1)
else:
    print(0)