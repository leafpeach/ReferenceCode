#exception Handling

from re import X #Ignore


try:
    print(x)
except:
    print("An exception occured") #Instead of an error, this will print

#If we just printed x, an actual error will occur

#we can have many exceptions

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

#Else keyword

try:
    print("Hello")
except NameError:
    print("Variable x is not defined")
else:
    print("Nothing went wrong")

#Finally state,emt

try:
    print(x)
except NameError:
    print("Variable x is not defined")
finally:
    print("The try except is finished")


#Can also be used to open and write to a file that is not writeable

try:
    f = open("testTxt")
    try:
        f.write("Lets add some text")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close
except:
    print("Something went wrong with opening the file") #This will print


#Raising an exception

x = -1

if x < 0:
    raise Exception("Sorry no numbers below 0")

y = "hello"

if not type(y) is int:
    raise TypeError("Only ints allowed") 


