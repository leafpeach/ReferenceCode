# Simple for loop

dbh_Characters = ["Connor", "Kara", "Markus"]
for x in dbh_Characters:
    print(x) #Will output Connor, Kara, Markus

#Loop through a string

for x in "Connor":
    print(x) #Will print each letter of Connor

#Break statement

for x in dbh_Characters:
    print(x)
    if x == "Kara":
        break #Loop will break once it iterates at Kara

#When the loops breaks before it can be printed

for x in dbh_Characters:
    if x == "Kara":
        break
    print(x)

#The continue statement

for x in dbh_Characters:
    if x == "Kara":
        continue
    print(x)

#The range() function

for x in range(6):
    print(x) #will print 0-5

#Adding the start parameter

for x in range(2,6):
    print(x) # will print 2-5

#Adding the step paramenter

for x in range(2, 30, 3):
    print(x) #Will increment to 30 by 3

#Using the else keyword

for x in range(6):
    print(x)
else:
    print("FInished")


#Using the else keyword with the break statement

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

#Nested for loops

superMario_Chars = ["Mario", "Luigi", "Peach"]

for x in dbh_Characters:
    for y in superMario_Chars:
        print(x, y)