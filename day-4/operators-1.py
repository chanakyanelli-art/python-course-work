Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======================================================== RESTART: C:/Users/CHANAKYA/Desktop/python-course-work/day-4/opertors.py =======================================================

======================================================== RESTART: C:/Users/CHANAKYA/Desktop/python-course-work/day-4/opertors.py =======================================================
a=20
b=10
a+b
30
a-b
10
a/b
2.0
9/2
4.5
54/2
27.0
9//2
4
a//b
2
a*b
200
a%b
0
27%8
3
a**b
10240000000000
b**a
100000000000000000000
26**65
94030255916461724219498599148081692997635349288323463430652507724653428878751010281148645376
6**3
216
a
20
b
10
a<b
False
a>b
True
b>a
False
a<=b
False
a>=b
True
a==b
False
a=b
a!=b
False
10<=b
True
a>=b
True
a==b
True
a!=b
False
#assignment
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y+=10
y
30
y-=10
y
20
y-=20
y
0
y+=20
y
20
y/=5
y
4.0
y+=26
y
30.0
y//=5
y
6.0
y+=16
y
22.0
y%=11
y
0.0
y+=10
y
10.0
y**=2
y
100.0
#logical
a
10
b
10
a=20
b=10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False
not a<b
True
#membership
#str,list,tuple,set,dict
a=('python programming')
a
'python programming'
'y' in a
True
'pro' in a
True
'chanu'
'chanu'
'chanu' in a
False
'on' not in a
False
l=['java','python','mysql','c++','c','html']
l
['java', 'python', 'mysql', 'c++', 'c', 'html']
'c' in a
False
'c' in l
True
'python' not in l
False
t=('laptop','mobile','mouse','keyboard')
t
('laptop', 'mobile', 'mouse', 'keyboard')
'key' in t
False
'keyboard' in t
True
'laptop' not in t
False
d={'egg':9,'oil':120,'sugar':40,'salt':25}
'oil' not in d
False
'sugar' in a
False
'sugar' in d
True
#identity
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
n==m
True
l is m
False
n is m
True
n is not m
False
n is not l
True
id(l)
2112686565696
id(m)
2112642862144
id(n)
2112642862144
l is not m
True
n is not l
True
#bitwise
8&4
0
8&14
8
8|7
15
>>> 10^12
6
>>> ~12
-13
>>> 8>>2
2
>>> 15>>1
7
>>> 15>>3
1
>>> 16<<2
64
>>> 4>>2
1
>>> a=12
>>> b=12.34
>>> c='python'
>>> print(a,b,c)
12 12.34 python
>>> print('a=',a,'b=',b,'c=',c)
a= 12 b= 12.34 c= python
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=12b=12.34c=python
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
12
b=
12.34
c=
python
>>> print('a=',a,'b=',b,'c=',c,sep='\n\n')
a=

12

b=

12.34

c=

python
>>> print('a=',a,'b=',b,'c=',c,sep='',end='@@@')
a=12b=12.34c=python@@@
>>> print(f'a={a} b={b} c={c}')
a=12 b=12.34 c=python
