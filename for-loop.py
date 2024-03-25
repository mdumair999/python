z=[6,4,3,8]
target=4 #subtract of 2 nums
for i in range(0,len(z)):
    for j in range(abs(-1), len(z)):
        if z[i] - z[j] == target:
            print (i,j)

