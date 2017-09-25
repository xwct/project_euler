num = 2520

while True:
    rem = 0
    for i in range(2, 21):
        rem += (num % i)
        
        if rem != 0:
            break
    if rem == 0:
        print(num)
        break
    num += 20
