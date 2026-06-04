Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='    hello   world   '
s
'    hello   world   '
s.strip()
'hello   world'
>>> s.lstrip()
'hello   world   '
>>> s.rstrip()
'    hello   world'
>>> #string testing method
>>> s='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('ghd')
False
>>> s.endswith('py')
True
>>> s.endswith('yp')
False
>>> 'sdfyui'.isalpha()
True
>>> 'DFGHJSGjhhjsjjjd'.isalpha()
True
>>> 'chanakya@635546'.isalpha()
False
>>> '12344'.isnum()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    '12344'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> '1223356'.islnum()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    '1223356'.islnum()
AttributeError: 'str' object has no attribute 'islnum'. Did you mean: 'isalnum'?
>>> '12345766'.isalnum()
True
>>> 'ejgjjhj'.islower()
True
>>> 'ajdhjhj@&%'.islower()
True
>>> 'DAHHGAHJ'.isupper()
True
>>> ' '.isspace()
True
>>> 'py_python'.isidentifier()
True
>>> 'py@123'.isidentifier()
False
