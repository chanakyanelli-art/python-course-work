
res1 = []
for i in range(1,11):
    res1.append(i)

res2 = [i for i in range(1,11)]

print(res1)
print(res2)

res3 = []
for i in range(3,31,3):
    res3.append(i)

res4 = [i for i in range(3,31,3)]

print(res3)
print(res4)

res5 = []
for i in range(2,51,2):
    res5.append(i)

res6 = [i for i in range(2,51,2)]

print(res5)
print(res6)


a = 'python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        
        l.append(i)
print(l)

ll = [i for i in a if i in 'aeiouAEIOU']
print(ll)
'''
l = [val for var in seq]
l = [val for var in seq if condition]
l = [val if condition else val for var in seq]
'''
a = [1,2,3,4,5,6,7,8,11,12,32,45,65,67,80]
l = []
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)

ll = [i if i%2==0 else 0 for i in a]
print(ll)


l = [int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)


l = []
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1 = [j for i in range(3) for j in range(1,4)]
print(l1)


l = [[j for j in range(1,4)]for i in range(3)]
print(l)


s = set()
for i in range(1,11):
    s.add(i)
s1 = {i for i in range(1,11)}
print(s,s1)


d = {}
for i in range(1,11):
    d[i]=i*i
print(d)

res = {i:i*i for i in range(1,11)}
print(res)


d = {}
for i in range(5):
    a = input()
    d[a]=int(input())
print(d)

res = {input():int(input()) for i in range(5)}
print(res)

