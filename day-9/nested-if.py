products = {
    'laptops':0,
    'mouse':10,
    'chrager':5,
    'phones':30,
    'keyboard':0
}

product = input("Enter the produt: ")
if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"{product} is out of stock")
else:
    print(f"{product} is not available")
