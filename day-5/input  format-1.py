Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
chanakya
name
'chanakya'
name = input("Enter your name: ")
Enter your name: chanakya
name
'chanakya'
age = input("Enter your age: ")
Enter your age: 21
age
'21'
type(age)
<class 'str'>
gpa = float(input("Enter the gpa: "))
Enter the gpa: 7.2
gpa
7.2
type(gpa)
<class 'float'>
'chanakya pandu prdeepp manideep'
'chanakya pandu prdeepp manideep'
names = input("Enter the name: ").split()
Enter the name: chanakya pandu prdeepp manideep
names
['chanakya', 'pandu', 'prdeepp', 'manideep']
products = input("Enter the productsL: ").split()
Enter the productsL: laptop mouse charger keyboard
produts
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    produts
NameError: name 'produts' is not defined. Did you mean: 'products'?
products
['laptop', 'mouse', 'charger', 'keyboard']
topic = tuple(input("Enter the topics: ").split())
Enter the topics: in not is is not and or not
topic
('in', 'not', 'is', 'is', 'not', 'and', 'or', 'not')
topics = tuple(input("Enetr the topics: ").spilt())
Enetr the topics: token statments variables comments
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    topics = tuple(input("Enetr the topics: ").spilt())
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
topics = tuple(input("Enetr the topics: ").split())
Enetr the topics: token statments variables comments
topics
('token', 'statments', 'variables', 'comments')
op = set(input("Enter the op: ").split())
Enter the op: in not is is not and or not
op
{'in', 'is', 'not', 'and', 'or'}
marks = input("Enter the marks: ").split())
SyntaxError: unmatched ')'
marks = input("Enter the marks: ").split()
Enter the marks: 34 25 53 76
marks
['34', '25', '53', '76']
int = int(input("enter your num: ").split())
enter your num: 4 5 3 6 7
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int = int(input("enter your num: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
list(map(int,input("Enter the marks: ").split()))
Enter the marks: 1 3 5 85 345
[1, 3, 5, 85, 345]
prices = tuple(map(int,input("Enter the prices: ").split()))
Enter the prices: 435 5474 658488 87
prices
(435, 5474, 658488, 87)
rating = set(map(int,input("Enetr the rating: ").spilt()))
Enetr the rating: 4 3 4 5 3 3 2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    rating = set(map(int,input("Enetr the rating: ").spilt()))
AttributeError: 'str' object has no attribute 'spilt'. Did you mean: 'split'?
rating = set(map(int,input("Enetr the rating: ").split()))
Enetr the rating: 4 3 4 5 3 3 2
rating
{2, 3, 4, 5}
per = list(map(int,input("Enter the per's: ").split()))
Enter the per's: 56.3 23.3 78.9 34.5
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    per = list(map(int,input("Enter the per's: ").split()))
ValueError: invalid literal for int() with base 10: '56.3'
per = list(map(float,input("Enter the per's: ").split()))
Enter the per's: 56.3 23.3 78.9 34.5
per
[56.3, 23.3, 78.9, 34.5]
prices = tuple(map(float,input("Enetr the prices: ").split()))
Enetr the prices: 567 7468 836638 9344 8589 98
prices
(567.0, 7468.0, 836638.0, 9344.0, 8589.0, 98.0)
prices = set(map(float,input("Enter the prices: ").split()))
Enter the prices: 53774 499 9283 9488
prices
{9488.0, 9283.0, 499.0, 53774.0}
a,b=10,20
a
10
b
20
a,b=[10,20]
a
10
b
20
a,b=(22,34)
a
22
b
34
username,password = input("Enter the username & password: ").split()
Enter the username & password: pandu chanu@323
username
'pandu'
password
'chanu@323'
a,b,c,d = list(map(int,input("Enetr the 4 sides: ").split()))
Enetr the 4 sides:  5 6 7 8
b
6
a
5
c
7
d
8
price,discount = list(map(int,input("Enter the price & discount: ").split()))
Enter the price & discount: 5367 3687.89
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    price,discount = list(map(int,input("Enter the price & discount: ").split()))
ValueError: invalid literal for int() with base 10: '3687.89'
price,discount = list(map(float,input("Enter the price & discount: ").split()))
Enter the price & discount: 537673 7498.87
price
537673.0
>>> discount
7498.87
>>> a = eval(input())
6746
>>> a
6746
>>> a = eval(input())
6438389.89
>>> a
6438389.89
>>> type(a)
<class 'float'>
>>> KeyboardInterrupt
>>> a = eval(input())
[1,2,3,4,5]
>>> a
[1, 2, 3, 4, 5]
>>> KeyboardInterrupt
>>> a = eval(input())
(2,4,5,6)
>>> a
(2, 4, 5, 6)
>>> 
... KeyboardInterrupt
>>> a = eval(input())
... {3:5,3:8,4:6}
SyntaxError: multiple statements found while compiling a single statement
>>> a = eval(input())
{3:5,4:6,5:6}
>>> a
{3: 5, 4: 6, 5: 6}
>>> a = eval(input())
true
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
