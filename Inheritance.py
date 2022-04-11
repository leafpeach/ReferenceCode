#Creating a parent class

class android:
    def __init__(a, first_name, last_name):
        a.firstname = first_name
        a.lastname = last_name

    def printname(a):
        print(a.firstname, a.lastname)


obj = android("Connor", "RK800")
obj.printname()

#Creating a child class

class mother(android):
    def __init__(b, first_name, last_name, releaseYear, daughter, enemy):
        android.__init__(b, first_name, last_name)
        b.first_name = first_name
        b.last_name = last_name
        b.releaseYear = releaseYear
        b.daughter = daughter
        b.enemy = enemy

    def meetKara(b):
        print("Hello " + b.first_name, b.last_name + ". Meet your daughter, " + b.daughter)

obj2 = mother("Kara", "AX200", 2031, "Alice", "I dunno")
obj2.meetKara()

