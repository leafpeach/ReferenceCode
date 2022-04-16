import re

#Check to see if the text starts with "This" and ends with "example"

txt = "This is a really cool example"
x = re.search("^This.*example$", txt)

if x:
    print("Matched")
else:
    print("Doesnt match")

#The findall() function returns a list containing all matches

y = re.findall("is", txt)

print(y)

z = re.findall("bad", txt)

print(z)

#The search() function

trueSentence = "Connor is sexy as heck"
a = re.search("sexy", trueSentence)

if a:
    print("Connor is in fact sexy")
else:
    print("Connor is not sexy (jk)")

#The split() function

b = re.split("is", trueSentence)

#maxsplit parameter

c = re.split("\s", trueSentence, 2)
print(c)

#sub() function

d = re.sub("Connor", "Markus", trueSentence)
print(d)

searching = re.search("is", trueSentence)
print(searching)

#.span() function

newTxt = "The rain in Spain"
x = re.search(r"\bS\w+", newTxt)
print(x.span())

#.string()

print(x.string)

#.group()

print(x.group()) #Looks for any word starting with S

