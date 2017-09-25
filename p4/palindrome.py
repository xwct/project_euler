num = 0
for i in range(1000):
    for j in range(1000):
        n = i * j
        if (str(n) == str(n)[::-1]):
            if n > num:
                num = n

    print(num)
