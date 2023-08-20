# string
# strings in python are surrounded by either single quotation or double quotation marks
# "heloo"  is same 'helo'
# import string
#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
print("helo")
print('heloo')

#1 multiple string:
# we can assign multiple string to paragraph
a="""There are some key Difference Between Local 
and Global Variable in Python: Global variables are declared 
outside the functions whereas 
local variables are declared within the functions. """
print(a)

#2 string slicing
e="heloo world"
print(e[2:5])     # position 2 to position 5(5 not included)
print(e[:5])      # position 0 to position 5 (5 not included)
print(e[2:])      # position 2 to position end
print(e[-5:-2])   # this is reverse slicing starting from reverse.last integer included

#3 modify string
# upper case
q=' Hello World '
print(q.upper())                        #for  upper case
print(q.lower())                        #for  lower case
print(q.strip())                        #remove white space from beginning or end
print(q.replace("H","j"))    # for using the replace the world
print(q.split(','))                     #for split the string

#5 string concatination
a="h"
b="eloo"
print(a+b)                             # result is heloo

#6 formating string
age=30
name="my name is ali and i am  {}"
print(name.format(age))               # my name is ali and i am  30

name="ahmad"
age=23
person="i am {} and my age is {}"
print(person.format(name,age))  # i am ahmad and my age is 23

name="ali"
age=20
person="i am {1} and my age is {0}"
print(person.format(name,age))  # i am 20 and my age is ali

#7 escape characer
# escape character allow to insert character that are illegal in string.
# a="my name "first" is ali"
# print(a)
a="my name \"first\" is ali"
print(a)
# Escape Sequence	   Meaning
# \\	               Backslash
# \n	               Newline
# \r	               Carriage Return
# \t	               Horizontal Tab

#8 string method
# there are many built in method that can use in sting