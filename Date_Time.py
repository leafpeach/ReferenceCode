#Importing datetime

import datetime

x = datetime.datetime.now()
print(x)

#Return the year and name of weekday

print(x.year)
print(x.strftime("%A"))

#How to create dates
#You can use the datetime() class of the datetime module
#The datetime() class requires 3 parameters

y = datetime.datetime(2000, 8, 7)
print(y)

#The strftime() Method
#Turns the integers into readable strings
#There is a reference chart for all legal format codes

print(x.strftime("%B"))