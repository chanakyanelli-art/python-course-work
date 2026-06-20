#local scope

def display():
    n=10
    print("Inside:",n)
display()
print("Outside:",n)

#global scope
n=10
def display():
    
    print("Inside:",n)
display()
print("Outside:",n)

def display():
    global n
    n=10
    print("Inside:",n)
display()
print("Outside:",n)


def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("Outside:",n)

#nonlocal
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("Outer funtion:",n)
outer()

s='python'
print(len(s))

len=5
print(len(s))


#int float compelx str list tuple set dict
#int float complex str tuple bool
#list set dict

def update(n):
    n={12}
    print("inside:",n)
n={23}
update(n)
print("outside:",n)

def update(n):
    n=2+5j
    print("inside:",n)
n=3+7j
update(n)
print("outside:",n)


def update(n):
    n=1.45
    print("inside:",n)
n=3.45
update(n)
print("outside:",n)


def update(n):
    n=[1,2,3]
    print("inside:",n)
n=[3,4,5]
update(n)
print("outside:",n)


def update(n):
    n={"laptop":1500}
    print("inside:",n)
n={"keyboard":800}
update(n)
print("outside:",n)

def update(n):
    n=False
    print("inside:",n)
n=True
update(n)
print("outside:",n)

