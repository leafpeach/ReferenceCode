# Example tuple

exampleTuple = ("This", "is", "an", "example")
print(exampleTuple)

#Tuples allow duplicates

exampleTuple_2 = ("two", "two", "one")
print(exampleTuple_2)

#Find the length of a tuple

print(len(exampleTuple_2))

#You can have a tuple with one item, but it has to have a comma after the last item

oneTuple = ("One",)
print(oneTuple)

#You can create a tuple with the .tuple() function

aTuple = tuple(("new", "tuple"))

#Access a tuple through indexing

print(exampleTuple[1])
print(exampleTuple[:1])
print(exampleTuple[0:])
print(exampleTuple[-3:-1])

#You can convert a tuple into a list to change it since tuples are immutable

newList = list(exampleTuple)
newList[1] = "hi"
exampleTuple = tuple(newList)

print(exampleTuple)

#You can combine a tuple

tuple_2 = ("another", "tuple")
exampleTuple += tuple_2
print(exampleTuple)

#Remove items by converting tuples into a list and changing it

y = list(exampleTuple)
y.remove("another")
exampleTuple = tuple(y)

#or you can delete the tuple

del exampleTuple

#You can unpack and pack items in a tuple which means you can give the values in a tuple their own variable
detroitCharacters = ("Connor", "Markus", "Kara") #This is a packed variable

(best, extravagent, wholesome) = detroitCharacters

print(best)
print(extravagent)
print(wholesome)

#Using asterisk. You can assign multiple values to one variable

superMarioChars = ("Luigi", "Bowser", "Peach", "Daisy", "Waluigi")

(green, red, *pink) = superMarioChars

print(green)
print(red)
print(pink)

fnafChars = ("Freddy", "Bonnie", "Chica", "Foxy", "Withered Bonnie", "Withered Freddy")

(brown, *purple, yellow) = fnafChars

print(brown)
print(purple)
print(yellow)

#Loop through a tuple

for x in detroitCharacters:
    print(x)

#Loop using the .range() and .len() function

for i in range(len(detroitCharacters)):
    print(detroitCharacters[i])

#WHile loop

i = 0
while i < len(detroitCharacters):
    print(detroitCharacters[i], i)
    i += 1

#Combine tuples

greatTuple = detroitCharacters + superMarioChars

print(greatTuple)

#Multiply Tuples

testTuple = ("Bunnies", "frogs", "snakes")
multiplyTuple = testTuple*2

print(multiplyTuple)


