from numpy import *

print('Enter data for first matrix')
a = int(input('enter number of rows: '))
b= int(input('enter number of colums: '))
ar1 = zeros((a,b))
for i in range(a):
    for j in range(b):
        ar1[i][j] = int(input("enter array values " +str(i)+ str(j)+":"))

print(ar1)


print("enter data for second matrix")
c = int(input('enter number of rows: '))
d= int(input('enter number of colums: '))
if b==c:
    ar2 = zeros((c,d))
    for i in range(c):
        for j in range(d):
            ar2[i][j] = int(input('enter array values '+str(i)+str(j)+':'))

    print(ar2)

    ar3 = zeros((a,d))

    
    for i in range(a):
        for j in range(d):
            for k in range(c):
                ar3[i][j] = ar3[i][j] + ar1[i][k]*ar2[k][j]

    print('Below is your matrix multiplication')    
    
    print(ar3)
else:
    print('Matrix aren\'t compatible for multiplication')