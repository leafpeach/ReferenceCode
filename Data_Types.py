#Types of data types

a = "String data type"
b = 88 #int data type
c = 88.4 #float data type

d1 = 4
d2 = 3
d_final = complex(d1, d2) #complex data type

e = ["one", "two", "three"] #List data type
f = ("one", "two", "three") #tuple data type

g = range(4) #range data type
h = {"name" : "Leif", "age": "117"} #dictionary data type

i = {"one", "two", "three"} #set data type
j = frozenset({"one", "two", "three"}) #frozen set data type
k = True #Bool data type

l = b"Bytes" #Bytes data type
m = bytearray(5) #Byte array data type
n = memoryview(bytes(5)) #memory view data type



print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d_final)
print(type(d_final))
print(e)
print(type(e))
print(e.index("one"))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(l)
print(type(l))
print(m)
print(type(m))
print(n)
print(type(n))


