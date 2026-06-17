'''
def function_name(arg):
    #stmts
    return

function_name(para)
'''

def wish(name):
    print(f'Welcome to the python course {name}!')
wish('chanakya')
wish('prdeep')
wish('praneeth')
wish('sevank')


def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"
print(iseven(12))
print(iseven(13))


def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int(input("Enter the number: "))
print("factorial:",factorial(num))

def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime Number"
    return f"{num} - Prime Number"
num = int(input("Enter the number: "))
print(isprime(num))

def display(name,email,pwd):
    print("name:",name)
    print("Email:",email)
    print("Password:",pwd)
display('chanakya','chanakyanelli@gmail.com','chanu@435')
display('chanakyanelli@gmail.com','chanakya','chanu@435')
display('chanakyanelli@gmail.com','chanu@435','chanakya')


def display(name,email,pwd):
    print("name:",name)
    print("Email:",email)
    print("Password:",pwd)
display(name='chanakya',email='chanakyanelli@gmail.com',pwd='chanu@435')
display(email='chanakyanelli@gmail.com',name='chanakya',pwd='chanu@435')
display(email='chanakyanelli@gmail.com',pwd='chanu@435',name='chanakya')


def display(name,email,pwd=''):
    print("name:",name)
    print("Email:",email)
    print("Password:",pwd)
display('chanakya','chanakyanelli@gmail.com','chanu@435')
display('chanakya','chanakyanelli@gmail.com')


def display(*names):
    print("names:",names)
display('chanakya','kumar','chanu')
display('kumar','chanakya')
display('chanakya')


def display(**names):
    print("names:",names)
display(k1='chanakya',k2='kumar',k3='chanu')
display(k1='kumar',k2='chanakya')
display(k1='chanakya')
