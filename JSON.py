import json
from tkinter.ttk import Separator

#some JSON array

x = '{ "name":"Leif", "age":117, "city":"Deez"}'

#translate into python

y = json.loads(x)

#The result will be a Python Dictionary

print(y)
print(y["age"])

#Python Dict

hamilton = {
    "Best": "Aaron Burr",
    "Worst": "Alexander Hamilton",
    "Underrated": "Hercules Mulligan"
}

#From Python to JSON

jsonArray = json.dumps(hamilton)

#Result is a json string

print(jsonArray)

#What you can convert Python objects to JSON strings

print(json.dumps({"name":"Connor", "Partner": "Hank"}))
print(json.dumps(["Connor", "Markus"]))
print(json.dumps(("Mario", "Luigi")))
print(json.dumps("Hello"))
print(json.dumps(69))
print(json.dumps(69.420))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Variable with all Python objects that can be converted into a JSON String

fun = {
    "name": "Luis",
    "age": 21,
    "single": False,
    "boyfriend": "Gavin",
    "taken": True,
    "jealous": ("Gavin's cat?", "Nines", "Idk the ppl in Gavin's life"),
    "pets": ["A", "cute", "kitty"],
    "ships": [
        {"Reed900": "1/10", "Overrated": True},
        {"Eli900": "11/10", "Underrated": True}
    ]

}

print(json.dumps(fun))

#You can make the add indents and separators

json.dumps(fun, indent=4, separators=(". ", " = "))

#You can also sort the results

print(json.dumps(fun, indent=4, sort_keys=True))
