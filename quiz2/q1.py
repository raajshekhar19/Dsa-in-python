x = [[3,5],"mimsy",2,"borogove",1]  # Statement 1
y = x[0:50] 
z = y                                # Statement 3
w = x                                # Statement 4
x[1] = x[1][:5] + 'ery'
y[1] = 4 
print(y)