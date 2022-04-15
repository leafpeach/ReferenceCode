#Example of a iterator

from re import A


testTuple = ("green", "blue", "pink")
testIterator = iter(testTuple)

#Not very effective

print(next(testIterator))
print(next(testIterator))
print(next(testIterator))

#You can iterate a string

myStr = "HankxConnor"
testIt_2 = iter(myStr)

print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))
print(next(testIt_2))

#Of course you can loop through iterables

for x in testTuple:
    print(x)

#Creating an iterator using classes

class ranNumbers:
    def __iter__(self):
        self.a = 1
        return self #will return 1

    def __next__(self):
        x = self.a
        self.a += 1
        return x #will return 1,2,3,4,etc.

myClass = ranNumbers()
newIter = iter(myClass)

print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter)) #Last one outputs 6

#You can stop iterations

class countClass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

count = countClass()
newIter_2 = iter(count)

for x in newIter_2:
    print(x)

