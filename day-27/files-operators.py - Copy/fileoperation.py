
file = open('sample.txt','r')

print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()


try:
    file = open('samples.txt','r')
except FileNotFoundError:
    print("File is not there")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

with open('sample.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()


with open('sample.txt','a') as file:
    file.write('pradeep\najay\nranjith')


with open('samples.txt','a') as file:
    file.write('pradeep\najay\nranjith')


with open('sample.txt','w') as file:
    file.write('pradeep\najay\nranjith')

with open('demo.txt','w+') as file:
    file.write('pradeep\najay\nranjith')
    file.seek(0)
    print(file.read())

with open('demo.txt','a+') as file:
    file.write('pradeep\najay\nranjith')
    file.seek(0)
    print(file.read())

with open('demo.txt','r+') as file:
    file.write('pradeep\najay\nranjith')
    file.seek(0)
    print(file.read())

'''
import os

#os.mkdir('Sample')
#os.rmdir('Sample')
'''         
