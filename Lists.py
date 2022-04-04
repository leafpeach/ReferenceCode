#Simple list
testList = ["Model S", "Model 3", "Model X", "Model Y"]
print(testList)

print(testList[0]) #Will output "Model S"
print(len(testList))

strList = ["Model S", "Model 3", "Model X", "Model Y"]
intList = [1, 2, 3, 4]
boolList = [True, False, False]

print(strList, " ", intList, " ", boolList)

specialList = ["Model Y", 56000, True]

#List Constructor

listMaker = list(("Model Y", "Model X", "Model 3"))

print(listMaker)

print(boolList[1])
print(boolList[-1])

rangeList = ["Model Y", "Model X", "Model 3", 1, 2, 3, 4]

print(rangeList[2:5])
print(rangeList[2:])
print(rangeList[:5])
print(rangeList[-5:-2])

if "Model Y" in rangeList:
    print("The Model Y is in the List")

#Change item list

rangeList[1] = "Toyota Camery"
print(rangeList) #Will replace "Model X" with "Toyota Camery"

rangeList[1:3] = "VW Jetta", "Audi"
print(rangeList) #Will replace "Toyota Camery" and "Model 3"

#Inserting items in a list without removing an item

insertList = ["This", "Is", "a", "list", "That", "Has", "Items"]
insertList.insert(2, "not") #"2" is the index where "not" will be placed
print(insertList)

#Append items 
#the append() function adds items to the end of the list

appendList = ["This", "Is", "a", "list", "That", "Has", "Items"]
appendList.append("wow")
print(appendList)

#You can combine two lists by using the extend() function

listOne = ["Detroit", "Become", "Human"]
listTwo = ["is", "a", "great", "game"]

listOne.extend(listTwo)
print(listOne)

#Remove an item from a list

listOne.remove("great")
print(listOne)

#Remove an item from its index using the pop() function

listOne.pop(3)
print(listOne)

#You don't have to specify an index value

listOne.pop()
print(listOne)

#The del keyword removes an indexed item too

del listOne[0]
print(listOne)

#And delete the list entirely

del listOne

clearList = ["hi", "new", "list"]
clearList.clear()

#You can loop through a list using a for loop

randomList = ["Markus", "Connor", "Kara"]

for x in randomList:
    print(x)

#loop through items using its index

for i in range(len(randomList)):
    print(randomList[i])

#loop through a list using a while loop

i = 0
while i < len(randomList):
    print(randomList[i], " ", i)
    i += 1

#Looping using list comprehension

[print(x) for x in randomList]

newList = ["Reed", "Anderson", "Fowler"]
newList_1 = []

for x in newList:
    if "s" in x:
        newList_1.append(x)
print(newList_1) #Will output "Anderson"

#Shortened version

newList_2 = [x for x in newList if "s" in x] #Will output "Anderson" ans well

print(newList_2)

newList_2 = [x for x in newList if x != "Reed"] #outputs both "Anderson" and "Fowler"
print(newList_2)

newlist_3 = [x if x != "Reed" else "Anderson" for x in newList_2]
print(newlist_3) #Will output "["Anderson, "Fowler"]"

#Sort Lists

sortingList = ["iPhone", "Android", "Twenty", "Orange"]
sortingList.sort()
print(sortingList)

#Sort lists with numbers

sortingList_Num = [33, 53, 12, 93, 21]
sortingList.sort()
print(sortingList_Num)

#Sorted list descending

sortingList.sort(reverse= True)
print(sortingList)

#Customize sort function

def sortingFunc(n):
    return abs(n-50)

listFunc = [33, 43, 133, 90, 65]
listFunc.sort(key= sortingFunc)
print(listFunc)

#Case sensitive sort

caseSensitive_Sort = ["Apple", "dig", "Roach", "zebra"]
caseSensitive_Sort.sort()
print(caseSensitive_Sort)

#Case insensitive sort

caseSensitive_Sort.sort(key= str.lower)
print(caseSensitive_Sort)

#Reverse order

sortingList.reverse()
print(sortingList)

#Copying a list

ogList = ["random", "word", "two"]

copyList = ogList.copy()
print(copyList)

#Or you can do this which is interesting

copyList_2 = list(ogList)
print(copyList_2)

#Combine two lists

listA = ["first", "list"]
listB = ["Second", "lists"]

listC = listA + listB
print(listC)

#Another way to join lists

for x in listB:
    listA.append(x)

print(listA)

#ANOTHER way to join lists

listA.extend(listB)
print(listA)