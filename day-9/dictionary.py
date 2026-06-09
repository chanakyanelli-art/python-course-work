Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d
{}
d[1]='iny'
d
{1: 'iny'}
d[12.3]='float'
d
{1: 'iny', 12.3: 'float'}
d=[]
d
[]
d={}
d
{}
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d['demo']='str'
d
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[3]='fdghjk'
d[4]=3+4j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:2,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'fdghjk', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 2, 2: 2}, 9: False}
d{}
SyntaxError: invalid syntax
d={}
d
{}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[1]
2
d={'chanu':89,'pandu':97,'pradeep':99,'ajay':96,'praneet':92,'sevank':94}
d
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94}
d.get('sevank')
94
d.get('kumar')
d
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94}
d.get('kumar','user not found')
'user not found'
d.get('chanu','user not found')
89
\
d.get('pandu','user not found')
97
'chanu' in d
True
'kumar' in d
False
'pradeep' not in d
False
d.keys()
dict_keys(['chanu', 'pandu', 'pradeep', 'ajay', 'praneet', 'sevank'])
d.values()
dict_values([89, 97, 99, 96, 92, 94])
d.items()
dict_items([('chanu', 89), ('pandu', 97), ('pradeep', 99), ('ajay', 96), ('praneet', 92), ('sevank', 94)])
sorted(d)
['ajay', 'chanu', 'pandu', 'pradeep', 'praneet', 'sevank']
max(d)
'sevank'
min(d)
'ajay'
len(d)
6
d
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94}
d['rishi'=88
  
SyntaxError: '[' was never closed
d['rishi']=88
  
d
  
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88}
>>> d['chanakya']=78
...   
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78}
>>> d.update({'sagar':90,'komali':98})
...   
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78, 'sagar': 90, 'komali': 98}
>>> d.popitem()
...   
('komali', 98)
>>> d.popitem()
...   
('sagar', 90)
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78}
>>> d.popitem()
...   
('chanakya', 78)
>>> del ['ajay']
...   
SyntaxError: cannot delete literal
>>> del d['ajay']
...   
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'praneet': 92, 'sevank': 94, 'rishi': 88}
>>> d.clear()
...   
>>> d
...   
{}
>>> d={'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78}
...   
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78}
>>> d.setdefault('syam',0)
...   
0
>>> d
...   
{'chanu': 89, 'pandu': 97, 'pradeep': 99, 'ajay': 96, 'praneet': 92, 'sevank': 94, 'rishi': 88, 'chanakya': 78, 'syam': 0}
