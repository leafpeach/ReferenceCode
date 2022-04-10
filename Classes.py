#Simple class syntax

class testClass:
    x = 5

#Creating objects

object1 = testClass
print(object1.x)

#The __init__() function

class android:
    def __init__(self, name, occupation, partner, partner_age):
        self.name = name
        self.occupation = occupation
        self.partner = partner
        self.partner_age = partner_age

androidObject = android("Connor", "Cop", "Hank", 54)

print(androidObject.name)
print(androidObject.partner)

#Object methods
#Note: the self parameter does not have to be named self

class detective:
    def __init__(self, name, partner, annoying):
        self.name = name
        self.partner = partner
        self.annoying = annoying
    
    def detectoveFunc(self):
        print("Detective " + self.name + " is in love with " + self.partner)

detectiveObject = detective("Gavin Reed", "RK900", True)
detectiveObject.detectoveFunc()

#Modify objects

detectiveObject.name = "Elijah"

print(detectiveObject.name)

#Delete object properties

del detectiveObject.partner

#You can use the pass statement in a clas as well

class passClass:
    pass



