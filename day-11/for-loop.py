#str list tuple set dict range()
'''
for var in seq:
    print(var)
'''

s = 'python peogramming'
for ch in s:
    print(ch)


l = ['sugar','salt','oil','eggs']
for i in l:
    print(i)


t = ('1.intro','2.Token','3.data types')
for i in t:
    print(i)


s = {'laptop','mouse','keyboard','phone'}
for i in s:
    print(i)


d = {'name':'chanu','batch':55,'skills':['python','mysql','java','html']}
for i in d:
    print(i,d[i])


#range(start,stop+1,step) => (0,n,1)

for i in range(1,11):
    print(i)


for i in range(2,51,2):
    print(i)


for i in range(5,101,5):
    print(i)


for i in range(20,0,-1):
    print(i)


for i in range(30,2,-2):
    print(i)


for i in range(6):
    print(i)


for i in range(1,50,2):
    print(i)


s = 'looping statements'

for i in range(len(s)):
    print(i,s[i])


l = [7,2,4,8,3,1,5]
for i in range(len(l)):
    print(i,l[i])


t = (7,2,4,8,3,1,5)
for i in range(len(t)):
    print(i,t[i])


s = 'looping'
for i in enumerate(s):
    print(i[0],i[1])

l = [72,4,8,3,1,5]
for i in enumerate(l):
    print(i[0],i[1])

t = (7,2,4,8,3,1,5)
for i in enumerate(t):
    print(i[0],i[1])

k = {7,2,4,8,3,1,5}
for i in enumerate(k):
    print(i[0],i[1])


for i in range(10):
    pass


for i in range(10):
    if i==5:
        break
    print(i)


for i in range(10):
    if i==5:
        continue
    print(i)


s = 'looping statements'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)


l = [56,76,32,3,34,2,3,5,97,45,23,98,76,32]
for i in l:
    if i%2==0:
        print(i)


d = {'laptops':0,'chargers':2,'keyboards':10,'phone':15,'tab':0,'mouse':5}
for i in d:
    if d[i]:
        print(i)


t = (9,2,13,4,5,6)
for i in range(len(t)):
    print(i*t[i])

names = {'chanu','pradeep','sevank','ajay','praneeth','ranjith'}
for i in names:
    print(i.upper())
