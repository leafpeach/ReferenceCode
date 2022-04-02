#Example of a simple, basic string

x = "This is an example of a string"
y = 'This is also an example of a string'
z = '''I can put
this string on
several lines omg'''

#Access an element in a string using square brackets

x1 = "Example"
print(x1[0])

#You can iterate/loop through a string using a for loop
#Here's a very simple for loop

for i in "example":
    print(i)

#You can check the length of a string using the len() function

y1 = "I wonder how many characters this sentence has"
print(len(y1))

# in and not in keywords
#They basically return a bool statement (True or False)
z1 = "This is a sentence"
print("sentence" in z1)

#Slicing strings (samurai slice)

sliced = "Lets slice this sentence"
print(sliced[1:8])

print(sliced[1:])
print(sliced[:8])

#Negative slicing starts at the end of your string

print(sliced[-5:-2])

#You can modify your string after creating it without going back and changing it

test_string = "Test sentence!"

print(test_string.upper())
print(test_string.lower())

test_string_space = " Whitespace "
print(test_string_space.strip())

print(test_string.split("sentence"))

#String concatenation

a = "One"
b = "Two"
c = a + b

print(c)

c2 = a + " " + b
print(c2)

# Concatenation with strings and numbers

age = 117
string = "My name is Leif and I am {}"
print(string.format(age))

#Escape characters

escape_string = "This is how you use \"escape\" characters"
print(escape_string)