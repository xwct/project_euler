square = 0

for i in range(101):
    square += i**2

sumsquare = sum(list(range(101)))**2
print(sumsquare-square)
