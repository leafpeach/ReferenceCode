myFile = open("testfile.txt", "r")
print(myFile.read())

#Reading only parts of a file

print(myFile.read(5))
print(myFile.readline())

#Loop through a file

for x in myFile:
    print(x)