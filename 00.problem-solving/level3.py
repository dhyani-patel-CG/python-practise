# level 3

# 21
n = int(input("enter a number: "))
if n < 0:
    n = -n
count = 0
if n == 0:
    count = 1
else:
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
print(count)