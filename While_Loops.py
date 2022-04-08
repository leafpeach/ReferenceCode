#Simple while loops

i = 1
while i < 6:
    print(i)
    i += 1 #Will stop at 5

#The break statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1 #Code will stop running after 3

#The continue statement

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i) # Will skip 3, and continue onto the next iteration

#The else statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is done iterating")


