#Example set

mySet = {"example", "example2", "example3"}

#Length of a set

print(len(mySet))

#Make a set

newSet = set(("brand", "new", "set"))

#Loop through a set

for x in newSet:
    print(x)

#You can check to see if an item is in a set

print("brand" in newSet)

#You can add items to sets

newSet.add("Awesome")
print(newSet)

#You can add another set to another by using the .update() function

newSet_2 = {"another", "set", "being", "added"}

newSet.update(newSet_2)
print(newSet)

#You can add any of the storage holders to a set

newList = ["a", "list"]
newTuple = ("fancy", "tuple")

newSet.update(newList, newTuple)

print(newSet)

#Remove an item from a set using the .remove() and .discard() function

newSet.remove("fancy")
print(newSet)

newSet.remove("another")
print(newSet)

#remove the last item of a set by using the .pop() function

newSet.pop()
print(newSet)

#clear or delete a set

newSet.clear()

del newSet #will raise an error if you try to print it

#Join two sets
#First we can use the .union() function

set1 = {2, 4, 3, 5}
set2 = {"mitski", "is", "great"}
set3 = set1.union(set2)

print(set3)

#You can use the .update() function as well

set2_1 = {"a", "b", "c"}
set3.update(set2_1)
print(set3)

#If you want to only keep the duplicates in a set, you can use the .intersection_update() function

a = {"Model X", "Model 3", "Model Y"}
b = {"Camery", "Jetta", "Model X"}

a.intersection_update(b)
print(a)

#The .intersection() function will return a new set

c = a.intersection(b)

print(c)

#If you want to keep all items except duplicates, use the symmetric_difference_update()

a.symmetric_difference_update(b)

print(a)

#The .symmetric_difference() function will return a new set

c2 = a.symmetric_difference(b)

print(c2)