'''
#method overloading:

class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, Welcome to the hotstar')
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You can selcet the language")
    def playcontrollers(self):
        print("You can pause and play the video")
    def ads(self):
        print("Ads will be run")
    def movies(self):
        print("You can limted access for movies")
    def sports(self):
        print("Limted time you can watch sports")
    def quality(self):
        print("Limted quality")
        
#method overriding:

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, Welcome to the Premium hotstar')
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can unlimted access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("High quality")
        

chanu = Hotstar('chanu')
chanu.login()
chanu.dashboard()
chanu.search()
chanu.languages()
chanu.playcontrollers()
chanu.ads()
chanu.movies()
chanu.sports()
chanu.quality()

pandu = PremiumHotstar('pandu')
pandu.login()
pandu.dashboard()
pandu.search()
pandu.languages()
pandu.playcontrollers()
pandu.ads()
pandu.movies()
pandu.sports()
pandu.quality()

#operator overloading:

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)
n1 = Number(10)
n2 = Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)


class Followers:
    def __init__(self, count):
        self.count = count
    def __add__(self, other):
        return Followers(self.count + other.count)
    def __str__(self):
        return f"Total Followers: {self.count}"
a1 = Followers(1800)
a2 = Followers(3000)

total = a1+a2
print(total)

'''

def upload_photo():
    print("Compressing photo...")
    print("uploading photo...")
    print("photo uploaded successfull!")

def upload_video():
    print("Encoding video...")
    print("uploading video...")
    print("video uploaded successfully!")

upload_photo()
upload_video()
    
