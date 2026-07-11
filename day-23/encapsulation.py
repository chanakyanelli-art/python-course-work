'''
class Flipkart:
    pass
chanakya = Flipkart()
praneeth = Flipkart()
pradeep = Flipkart()
'''
class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showProducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")
chanakya = Flipkart()
chanakya.login('chanakya','chanakya@45')
chanakya.banner()
chanakya.showProducts()

Flipkart.showProducts()
Flipkart.banner()

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to the Instagram, {self.username}')

chanu = Instagram('chanu','chanu@123')


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []
    def getpassword(self):
        return self.__password
    def stepassword(self,newpassword):
        self.__password = newpassword

chanu = Instagram('chanu','chanu@123')

print("Before username:",chanu.username)
chanu.username = 'pandu'
print("After username:",chanu.username)

print("Before password:",chanu.getpassword())
chanu.setpassword='pandu@123'
print("After password:",chanu.getpassword())


class Instagram:
    def __init__(self):
        self._post = []

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

chanu = Instagram()
print(chanu.accesspost)
chanu.accesspost = 'class and object'
print(chanu.accesspost)
