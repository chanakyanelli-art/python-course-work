#match
import re

pattern = '[abc]'
text = 'codegnan'

res = re.match(pattern,text)
print(res.group() if res else "No Match Found")

#search
import re

pattern = '[a-z]'
text = 'Python version 3.11'

res = re.search(pattern,text)
print(res.group() if res else "No Match Found")

#findall
import re

pattern = '[0-9]'
text = 'Python version 3.11'

res = re.findall(pattern,text)
print(res)

#finditer
import re

pattern = '[0-9]'
text = 'Python version 3.11'

res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())

#fullmatch
import re

pattern = '[a-z]{9}'
text = 'abcdefghi'

res = re.fullmatch(pattern,text)
print(res.group() if res else "No Match Found")

#split
import re

pattern = r'[,a+yn]'
text = 'java,python,c++'
res = re.split(pattern,text)
print(res)

#sub
import re
pattern = r'[0-9]{2}'
text = 'python:34 mysql:78 java:55 html:45'

res = re.sub(pattern,'**',text)
print(res)
