z=[6,4,8]
target =4 #subtract of 2 nums output should be (2,1)
for i in range(0,len(z)):
    for j in range(i-1, len(z)):
        if z[i] - z[j] == target:
            print (i,j)


