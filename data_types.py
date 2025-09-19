#string data type

#literal alignment

first = "Dave"
last = 'Smith'

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza)==str)
# print(isinstance(pizza,str))

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)


statement = "I like the music of " + decade + "s."
print(statement)

#multiline 
multiline = """
Hey how are you?
I was just checking in. 
                            All good?
"""

print(multiline)

#escaping special characters
sentence = 'I\'m back at work! \t Hey \n\nWhere\'s this at\\located?'
print(sentence)

#string Methods

print(first)
print(first.lower())
print(first.upper())
print(first)


print(multiline.title())
print(multiline.replace("good","okay"))
print(multiline)

print(len(multiline))
multiline += "                                         "
multiline = "                       " + multiline
print(len(multiline))

print(multiline.strip())
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
#build a menu
title = "menu".upper()
print(title.center(20, "="))