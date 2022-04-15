#Local Scope

def bestDBH_Char():
    x = "Markus"
    print(x)

bestDBH_Char()
#if you print(x), it will result in an error because it is not in scope

def hotDBH_Char():
    x = "Connor"
    def printFunc():
        print(x)
    printFunc()

hotDBH_Char()

#Global Scope

x = "Kara"

def motherDBH_Char():
    x = "Rose"
    print(x) #Will print Rose

motherDBH_Char()

print(x) #Will print Kara

#Global keyword
y = "Mario, not so best boy"
def superMario_Char():
    global y 
    y = "Luigi, Best Boy"

superMario_Char() #Will print Luigi
print(y) #Will also print Luigi