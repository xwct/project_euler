# find a+b+c = 1000
# where aˆ2 + bˆ2 = cˆ2
# and a < b < c
# find a*b*c

d = 0
e = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if ((a**2 + b**2) == c**2):
            d = a + b + c
            e = a * b * c
            if d == 1000:
                print(a, b, c, d, e)
                break
    else:
        continue
    break
