# cheated a little, three years without math couldn`t remember how to prime factorize

num = 600851475143
fac = 0
i = 2

while i*i <= num:
    while (num % i) == 0:
        num = num / i
    print(num)
    i = i + 1
    
print(num)
