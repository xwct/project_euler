i = 1 
num = 2
while i <= 10001:
    numsq = int((num**0.5)//1)+1
#    print(num, numsq, i)
    
    for j in range(2, numsq):
#        print(j)
        if (num % j) == 0:
#            print("no prime here")
            break
    else:
#        print("Prime ",i, ":", num)
        i += 1
    num += 1
print(num-1)
