#A lambda function

x = lambda a : a + 10

print(x(5)) #Will output 15

#Multiple arguments

y = lambda a, b : a * b
print(y(4, 5))

z = lambda a, b, c : a + b + c
print(z(3, 2, 7))

#Lambdas are better inside of functions

def testFunction(n):
    return lambda a : a * n

num = testFunction(9)
print(num(7))

#You can have different values

num1 = testFunction(2)
num2 = testFunction(3)

print(num1(5))
print(num2(5))



