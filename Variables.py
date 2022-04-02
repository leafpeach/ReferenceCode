from tkinter import Y

#Simple Variables

my_Var = "My variable"
my_Num = 77
my_Float = 77.0
x = 5
y = 4
z = x+y

print(my_Var)
print(my_Num)
print(z)

#Multiples Values assigned to one varibale

multi_Vars = "These", "are", "multiple", "values"
print(multi_Vars)

#Multiple variables assigned to one value

x_One = y_Two = z_Three = "One variable"
print(x_One, y_Two, z_Three)


#Global Variables (No need to know what a function is yet)

def example_Func():
    global example_ #The global variable allows variables outside of functions work, whereas if example_ was not global, we would not be able to print it on line 36
    example_ = "Testing"
    print(example_)

example_Func()
print(example_)