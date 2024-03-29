#fators of a number
x = 10
l1 = []
for i in range(1 , x+1):
    if x % i == 0:
        l1.append(i)
print(l1)