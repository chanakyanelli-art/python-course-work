Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python Programming'
len(s)
18
min(s)
' '
max(s)
'y'
sorted(s)
[' ', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 't', 'y']
ord('a')
97
char(8)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    char(8)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(8)
'\x08'

s='python Programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.captlize()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.captlize()
AttributeError: 'str' object has no attribute 'captlize'. Did you mean: 'capitalize'?
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
"DYJIDHI#$SIhhhj".casefold()
'dyjidhi#$sihhhj'
s
'python Programming'
s.center
<built-in method center of str object at 0x000002042AD394B0>
s.center(38,'*')
'**********python Programming**********'
s.cenetr(28,'-')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.cenetr(28,'-')
AttributeError: 'str' object has no attribute 'cenetr'. Did you mean: 'center'?
s.center(28,'-')
'-----python Programming-----'
s.ljust(28,'-')
'python Programming----------'
s.rjust(28,'-')
'----------python Programming'
'123'zfill(5)
SyntaxError: invalid syntax
>>> '123'.zfill(5)
'00123'
>>> '1234'.zfill(9)
'000001234'
>>> s.find('p')
0
>>> s.rfind('m')
14
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s
'python Programming'
>>> s.count('y')
1
>>> s.count('m')
2
>>> s.count('g')
2
>>> s
'python Programming'
>>> s.replace('python','java')
'java Programming'
>>> s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
>>> s.translate(s.maketrans('python','123456'))
'123456 Pr5grammi6g'
>>> s='java,python,c,c++'
>>> s.split('-')
['java,python,c,c++']
>>> s.split(',',2)
['java', 'python', 'c,c++']
>>> s.splitlines()
['java,python,c,c++']
>>> l=['lava','python','javascript','c','c++']
>>> ''.join(l)
'lavapythonjavascriptcc++'
>>> '-'.join(l)
'lava-python-javascript-c-c++'
>>> '@'.join(l)
'lava@python@javascript@c@c++'
>>> ','.join(l)
'lava,python,javascript,c,c++'
