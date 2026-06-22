'''
#syntax
var = lambda agr: exp
'''
add = lambda a,b: a+b
print(add(23,13))
print(add(12,31))


wish = lambda name: f'Welcome the python course {name}'
print(wish('chanu'))
print(wish('pandu'))


gst = lambda price: price + price*0.18
print(gst(1000))
print(gst(500))
print(gst(79000))

greatest = lambda a,b: a if a>b else b
print(greatest(18,19))
print(greatest(2200,1900))
print(greatest(10,30))


iseven = lambda a: f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(9))
print(iseven(65))


bill = lambda charge: charge if charge>99 else charge + 30
print(bill(520))
print(bill(43))
print(bill(14))


login = True
instock = True
status = lambda login,instock :("You can by product" if instock else "Product is out of stock") if login else "Login to buy a product"
print(status(login,instock))


l=[1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)


names = ['chanu','pandu','chanakya']
t = list(map(lambda i:i.title(),names))
print(t)


l=[1,2,3,4,5,6,7,8,9,10,11,12]
res = list(filter(lambda i:i%2==0,l))
print(res)

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3==0,l))
print(res)

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s = reduce(lambda sum,i: sum+i,l)
p = reduce(lambda pro,i: pro*i,l)
m = reduce(lambda max,i: max if max>i else i,l)
mi = reduce(lambda max,i: max if max<i else i,l)
print(s,p,m,mi)


d = {'chanu':60,'pandu':50,'kumar':70,'pavan':40,'ganesh':80}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))


d = {'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res = dict(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1 = dict(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)


d = {'sugar':40,'salt':20,'cooking oil':80,'chilli':60}
res = dict(filter(lambda i:i[1]>50,d.items()))
res1 = dict(filter(lambda i:i[1]<50,d.items()))
print(res,res1)

