
#1
n = int(input())
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#2
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for j in range(n-i):
            print('*',end=' ')
    print()

#3
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
       print('* '*(i+1),end=' ')
    else:
       print('* '*(n-i),end=' ')
    print()
#4
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('*'*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('*'*(n-i),end=' ')
    print()

#5
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('* '*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('* '*(n-i),end=' ')
    print()

#6
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i)+'*  '*(i+1),end=' ')
    else:
        print(' '*(i-m)+'*  '*(n-i),end=' ')
    print()

#7
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j==m or i==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#8
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j==i or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#9
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or j==n or j==i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#10
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or j==0 or j==n-1 or j==n or j==i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


