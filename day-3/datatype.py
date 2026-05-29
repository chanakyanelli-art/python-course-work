Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
b=567.897
type(b)
<class 'float'>
c=5+8j
type(c)
<class 'complex'>
k='python'
type(k)
<class 'str'>
u="hfkkkd"
type(u)
<class 'str'>
m='''pandu'''
type(m)
<class 'str'>
>>> l=['chanu.py','jfdjj.jdh']
>>> type(l)
<class 'list'>
>>> l
['chanu.py', 'jfdjj.jdh']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,34,5,6,7)
>>> t
(1, 2, 34, 5, 6, 7)
>>> type(t)
<class 'tuple'>
>>> s={2,4,5,2,2,4}
>>> type(s)
<class 'set'>
>>> s
{2, 4, 5}
>>> s=set()
>>> a
10
>>> b
567.897
>>> s={356,65,53636,7357}
>>> s
{65, 53636, 356, 7357}
>>> d={'name':'abc','age':22,'course':'pfs'}
>>> type(d)
<class 'dict'>
>>> d
{'name': 'abc', 'age': 22, 'course': 'pfs'}
>>> status=True
>>> status=False
>>> type(ststus)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type(ststus)
NameError: name 'ststus' is not defined. Did you mean: 'status'?
>>> type(status)
<class 'bool'>
>>> a=None
>>> type(a)
<class 'NoneType'>
