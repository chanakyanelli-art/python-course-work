Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programmin lang'
s
'python programmin lang'
type(s)
<class 'str'>
s=''
s
''
a='codegnan'
b='pfs'
a+b
'codegnanpfs'
a
'codegnan'
a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'*'*20
'********************'
'python'*7
'pythonpythonpythonpythonpythonpythonpython'
names = ('chanu pandu pradeep sevank')
names
'chanu pandu pradeep sevank'
names[2,5]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    names[2,5]
TypeError: string indices must be integers, not 'tuple'
>>> names[2]
'a'
>>> names[234]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names[234]
IndexError: string index out of range
>>> names[-12]
'a'
>>> names[5]
' '
>>> names
'chanu pandu pradeep sevank'
>>> names[-7]
' '
>>> names[4:6]
'u '
>>> names[0:9]
'chanu pan'
>>> names[-4:-12]
''
>>> names[-12:-3]
'adeep sev'
>>> names[ :7]
'chanu p'
>>> names[-6: ]
'sevank'
>>> names[4::-1]
'unahc'
>>> names[13:4:1]
''
>>> names[13:4:-1]
'rp udnap '
>>> names[::-1]
'knaves peedarp udnap unahc'
>>> len(names)
26
>>> names.upper()
'CHANU PANDU PRADEEP SEVANK'
>>> names.lower()
'chanu pandu pradeep sevank'
>>> max(names)
'v'
