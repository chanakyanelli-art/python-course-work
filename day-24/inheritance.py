
#1.single inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

pandu = whatsappv1()
print("v1 = Pandu")
pandu.message()

chanu = whatsappv2()
print("v2 - Chanu")
chanu.message()
chanu.calls()

#2.mulitple inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")
        
class whatsappv3:
    def media(self):
        print("You can do photos/videos")

class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share-[24 hours]")
        
pandu = whatsappv4()
print("v4 - Pandu")
pandu.message()
pandu.calls()
pandu.media()
pandu.status()

#3.multilevel inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")
        
class whatsappv3(whatsappv2):
    def media(self):
        print("You can do photos/videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can share-[24 hours]")
        
pandu = whatsappv4()
print("v4 - Pandu")
pandu.message()
pandu.calls()
pandu.media()
pandu.status()

pandu = whatsappv2()
print("v2 - Pandu")
pandu.message()
pandu.calls()

pandu = whatsappv3()
print("v3 - Pandu")
pandu.message()
pandu.calls()
pandu.media()

pandu = whatsappv1()
print("v1 - Pandu")
pandu.message()

#4.hierarchical inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

pandu = whatsappv3()
print("v3")
pandu.message()
pandu.stickers()

pandu = whatsappv2()
print("v2")
pandu.message()
pandu.emojis()

pandu = whatsappv1()
print("v1")
pandu.message()

#5.hibrid inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
        print("You can send messages with gif to people")

pandu = whatsappv4()
print("v4")
pandu.message()
pandu.stickers()
pandu.emojis()
pandu.gif()

#method overriding:
#with super

class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

chanu = wpv3()
chanu.status()

#with out super
class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2:
    def status(self):
        print("You can react and reply")

class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("You can like and reshare")
pandu = wpv3()
pandu.status()


        
