Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t()
TypeError: 'tuple' object is not callable
t=()
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.1,'tyr',[])
t
(1, 1.1, 'tyr', [])
t=(10,20,30,40,50)
t[1]
20
t[4]
50
t[2]
30
t[5]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t[5]
IndexError: tuple index out of range
h=(90,70,60)
h
(90, 70, 60)
t+h
(10, 20, 30, 40, 50, 90, 70, 60)
t[1]
20
t*4
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t*6
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
30 in t
True
60 not in t
True
10 not in t
False
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(10)
0
t = 1,2,3,4,5,6,7
t
(1, 2, 3, 4, 5, 6, 7)
a,b,c=2,3,4
a
2
b
3
c
4
a = (1,2,30)
a
(1, 2, 30)
x,y,z=a
x
1
y
2
z
30
t=(1,2,3,[4,5,6],7,8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[2]=4
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3]
[4, 5, 6]
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
#set
s={1,2,3,4}
a
(1, 2, 30)
s
{1, 2, 3, 4}
s=set()
s={1,1,1,1,1,1}

s
{1}
s={987,,654,345,56,345,1,2,34,56}
SyntaxError: invalid syntax
s={987,,654,345,56,345,1,2,34,56}
s={987,654,345,56,345,1,2,34,56}
s
{1, 2, 34, 56, 345, 987, 654}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add("fkj")
s
{56.567, 1, 'fkj'}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add((1,2,3,4))
s
{56.567, 1, (1, 2, 3, 4), 'fkj'}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add((2,3,4,5))
s
{1, (1, 2, 3, 4), (2, 3, 4, 5), 56.567, 'fkj'}
s.add[:3]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.add[:3]
TypeError: 'builtin_function_or_method' object is not subscriptable
s.add(:3)
SyntaxError: invalid syntax
s.add(0:3)
SyntaxError: invalid syntax
1 in s
True
2 in s
False
False not in s
True
a={1,2,3,4,5,6,7,8}
b={6,7,8,9}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{8, 6, 7}
a & b
{8, 6, 7}
a - b
{1, 2, 3, 4, 5}
a ^ b
{1, 2, 3, 4, 5, 9}
a
{1, 2, 3, 4, 5, 6, 7, 8}
#{1}{2}{3}{4}{5}{1,3}{1,2}{8,10}\
a <={1}
False
a >={1}
True
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint(90,80)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    a.isdisjoint(90,80)
TypeError: set.isdisjoint() takes exactly one argument (2 given)
a.isdisjoint({90,80})
True
a
{1, 2, 3, 4, 5, 6, 7, 8}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 8, 17}
a.add(34)
a
{1, 2, 3, 4, 5, 6, 7, 8, 34, 17}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 6, 7, 8, 34, 11, 12, 13, 17}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 6, 7, 8, 34, 11, 12, 13, 17}
a.remove(10)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    a.remove(10)
KeyError: 10
a.remove(8)
>>> a
{3, 4, 5, 6, 7, 34, 11, 12, 13, 17}
>>> a.discard(10)
>>> a
{3, 4, 5, 6, 7, 34, 11, 12, 13, 17}
>>> a.discard(3)
>>> a
{4, 5, 6, 7, 34, 11, 12, 13, 17}
>>> a.clear()
>>> a
set()
>>> a={1,23,4,57,235}
>>> a
{1, 4, 23, 57, 235}
>>> b={1,2,4,34}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d = c.copy()
>>> d
{1, 2, 34, 4, 12}
>>> d.add(10)
>>> d
{1, 2, 34, 4, 10, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
