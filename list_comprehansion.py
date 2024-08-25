x = int(input())
y = int(input())
z = int(input())
n = int(input())

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                print([i,j,k],end=",")

#shortcut method
def fun(x, y, z, n):
    new_list = [[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
    print(new_list)


fun(x, y,z,n)