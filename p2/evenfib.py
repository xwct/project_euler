one = 1
two = 2
num = 0
tot = 2

while num<4000000:
    num = one + two
    one = two
    two = num
    if (num % 2) == 0:
        tot = tot + num
print(tot)
