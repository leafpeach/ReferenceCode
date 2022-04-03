#Boolean values are true and false statements

print(7==7)
print(7>8)
print(7<8)

x = 200
y = 33

if y < x:
    print("y is less than x")
else:
    print("x is less than y")

#Most things in Python will return True except:
#All of these inputs will return False

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# examples that will return a bool value
#you will not have to know what these are yet, they're just examples

class myClass():
    def __len__(self):
        return 0

myObj = myClass()
print(bool(myObj))
#Will output False

def testFunction():
    return True

print(testFunction()) #Will return True of course

if testFunction():
    print("This is True")
else:
    print("Not True")

#You can check a data type and it will return a Bool value

x = 200
print(isinstance(x, int))
print(isinstance(x, str))