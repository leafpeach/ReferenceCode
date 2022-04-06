#Example dictionary

newDict = {
    "brand": "Toyota",
    "model": "Camry",
    "year": "2022"
}

#You print the brand key of the dictiony

print(newDict["brand"])

#Determine the length of a dictionary

print(len(newDict))

#Dictionaries can have all of the data types inside them

newDict_2 = {
    "Connor": 30,
    "Android": True,
    "Kara": 29,
    "colors": ["pink", "blue", "white"]
}

print(newDict_2)

#Access items in a dictionary using it's key name

android = newDict_2["Android"]

#You can also use the .get() function

kara = newDict_2.get("Kara")

#You can return the list of keys

keys = newDict_2.keys()
print(keys)

newDict_2["Markus"] = "RA9"
print(newDict_2)

#You can get the values as well

print(newDict_2.values())

newDict_2["Android"] = "Ralph"

print(newDict_2)

#Use the .items() function to return each item in a list and it will output as a tuple

d = newDict_2.items()
print(d)

#Check to see if a key exists

if "Android" in newDict_2:
    print("android is here")
else:
    print("android not here")

#You can change the values in a dictionary

newDict_2["Markus"] = "Simon"
print(newDict_2)

#You can also use the .update() function

newDict_2.update({"Kara": "Alice"})
print(newDict_2)

#Removing items in a dictionary

newDict_2.pop("Kara")
print(newDict_2)

#The .popitem() function will remove the last item in the dictionary

newDict_2.popitem()
print(newDict_2)

#You can also use the del keyword to delete a key

del newDict_2["Android"]
print(newDict_2)

#You can clear a dictionary too using the .clear() function

newDict_2.clear()
print(newDict_2)

for x in newDict:
    print(newDict[x]) #Will print the values

#You can print out the either the keys or values

for x in newDict.keys():
    print(x)

for x in newDict.values():
    print(x)

for x, y in newDict.items():
    print(x,y)

#You can copy lists as well using the .copy() function and dict() function

coolDict = newDict.copy()
print(coolDict)

coolDict_2 = dict(newDict)

print(coolDict_2)

#Netsed dictionaries

videoGames = {
    "Couple":  {
    "Luigi": "Young brother",
    "Daisy": "Princess"
    },

    
    "DBH": {
    "Kara": "Mother",
    "Markus": "RA9"
    }, 


    "Toontown": {
    "Coach Zucchinni": "Coach",
    "Lil Oldman": "Annoying"
    }
}

print(videoGames["Couple"])

#Or you can do it this way

number_1 = {
    "name": "Connor",
    "Occupation": "Cop"
}

number_2 = {
    "name": "Kara",
    "Occupation": "Mother"
}

number_3 ={
    "name": "Markus",
    "Occupation": "Deveiant Leader"
}

DBH_Characters = {
    "Fav": number_1,
    "Amazing": number_2,
    "The Greatest": number_3
}

print(DBH_Characters)