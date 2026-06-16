
#string

s = 'python'
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')
        
#list

l=[[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in l:
    for j in i:
        sum+=j
print(f'sum = {sum}')

#dictionary

d={
    '1234':{'pin':'4567','balance':2300},
    '2345':{'pin':'9876','balance':5300},
    '3456':{'pin':'5678','balance':6300},
    '4567':{'pin':'9876','balance':7300}

    }
for i in d:
    print('Account number:',i)
    print('Pin number:',d[i]['pin'])


