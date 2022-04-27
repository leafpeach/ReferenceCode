#Easy Madlibs

name = input("Input a name: ")
adjective = input("Input an adjective: ")
noun = input("Input a plural noun: ")
noun_2 = input("Input another noun: ")
color = input("Input a color: ")
article_of_clothing = input("Input an article of clothing(singluar): ")
adjective_1 = input("Input an adjective: ")
adjective_2 = input("Input a second adjective: ")


madlib = "{} is a {} person and they smell like {}.\n Whenever I see them, they're always wearing a {} {}. \nEven though they're {}, I still think they're a {} person."

print(madlib.format(name, adjective, noun, color, article_of_clothing, adjective_1, adjective_2))