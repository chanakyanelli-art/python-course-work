'''
# . pattern
import re
pattern = r'h.t\b'
text = 'hot hit het hrt hat hate hood heart hjt h$t'
res = re.findall(pattern,text)
print(res)

# ^ pattern
import re
pattern = r'^h'
text = 'hot hit het hrt hat hate hood heart hjt h$t'
res = re.findall(pattern,text)
print(res)

# $ pattern
import re
pattern = r'j$'
text = 'hot hit het hrt hat hate hood heart hjt h$t'
res = re.findall(pattern,text)
print(res)

# * pattern
import re
pattern = r'ab*'
text = 'hot hit het hrt hat hate hood heart hjt h$t'
res = re.findall(pattern,text)
print(res)

# + pattern
import re
pattern = r'to+'
text = 'too to toooo toooooo'
res = re.findall(pattern,text)
print(res)

# ? pattern
import re
pattern = r'to?\b'
text = 'too to toooo toooooo'
res = re.findall(pattern,text)
print(res)

import re
pattern = r'[a-z]{4,5}'
text = 'serdfgh fghj fghj ghjkl dfghj'
res = re.findall(pattern,text)
print(res)

import re
pattern = r'(python)'
text = 'pyth pythn python puthon'
res = re.findall(pattern,text)
print(res)


import re
pattern = r'^[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'
text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid formate" if res else "Invalid format")
'''
#email
import re
pattern = r'^[a-zA-z0-9._]+@[a-zA-z0-9._]+\.[a-zA-z]{2,}$'
text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid formate" if res else "Invalid format")
'''
#password
import re
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@#$%^&+=!]).{8,}$'
text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid formate" if res else "Invalid format")

#number
import re
pattern = r'^[6-9]\\d{9}$'
text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid formate" if res else "Invalid format")

#username
import re
pattern = r'^[a-zA-Z0-9]{5,15}$'
text = input("Enter the text: ")
res = re.fullmatch(pattern,text)
print("Valid formate" if res else "Invalid format")
'''
