a = int(input())

hour = 9
minute = 0

for i in range(1, a + 1):
    minute += 45
    if i != a:
        if i % 2 == 0:
            minute += 15
        else:
            minute += 5

hour += minute // 60
minute -= (hour - 9) * 60

print(str(hour) + " " + str(minute))