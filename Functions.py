#Function syntax

def myFunction():
    print("Hello from the function")

#How to call a function

myFunction()

#Function parameters

def DBH_Ship(first_name):
    print(first_name + " x Hank")

DBH_Ship("Connor")

#A function with two parameters

def DBH_Ship2(one, two):
    print(one + " x " + two)

DBH_Ship2("Elijah", "Alexander")

#Arbitrary arguments

def DBH_Chars(*chars):
    print("The best Detroit character is " + chars[2])

DBH_Chars("Connor", "Kara", "Markus") #Will output Markus

#Keyword Arguments

def DBH_Chars2(char1, char2, char3):
    print("The best dbh character is " + char3)

DBH_Chars2(char1 = "Connor", char2 = "Kara", char3 = "Markus")

#Arbitrary keyword arguments

def superMario(**brother):
    print("The best brother is " + brother["fname"])

superMario(fname = "Luigi", lname = "Mario")

#Default parameter value

def superMarioChar(brother = "Luigi"):
    print("The best character is " + brother)

superMarioChar()
superMarioChar("Bowser")
superMarioChar("Daisy")
superMarioChar("Peach")

#Passing a lists as an argument

def sonicChars(movie):
    for x in movie:
        print(x)

movie = ["Sonic", "Tails", "Knuckles"]

sonicChars(movie)

#Return statement

def testFunction(num):
    return 5 * num

print(testFunction(3))
print(testFunction(5))
print(testFunction(9))

#Pass statement

def passFunction():
    pass

#Recursion Example

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(3)

#We start with tri_recursion(3)
#3 + tri_recursion(2)
#3 + 2 + tri_recursion(1)
#3 + 2 + 1

#ANother recursion example

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num = 3
print(factorial(num)) #Outputs 6

#We start out with factorial(3)
#3 * factorial(2)
#3 * 2 * factorial(1)
#3 * 2 * 1
# Outputs 6