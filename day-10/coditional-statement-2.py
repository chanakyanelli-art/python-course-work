data ={
    'chanu':{'status':True,'python':98,'mysql':95,'flask':94},
    'praneeth':{'status':True,'python':88,'mysql':65,'flask':74},
    'pradeep':{'status':False,'python':None,'mysql':None,'flask':None},
    'sevank':{'status':True,'python':68,'mysql':75,'flask':84},
    'ajay':{'status':True,'python':33,'mysql':25,'flask':34},
    }
name = input("Enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg = total/3
        if avg > 90:
            print(f"Congrations {name}, you got first class!!!")
        elif avg > 70:
            print(f"Good {name}, keep it up for the next time!!")
        elif avg > 35:
            print(f'Better {name}, work hard next time!')
        else:
            print(f'{name}, you have failed in the exam. Bring your parents.')
    else:
        print(f"{name} didn't write the exam. Bring your parents")
else:
    print(f"{name}'s data is not found")
        
