# tuples
# tuples are use to store multiple item in single variable
# a tuples is collection of ordered item which can not be change
# tuples are written in round brackets.
tuples=("ali","ahmad","hassan")
print(tuples)                           # ('ali', 'ahmad', 'hassan')
print(len(tuples))                      # 3
# to create a tuple in single item use comma ohterwise it recongnize as str
name=("ali")                            # is atr
name1=("ali",)
print(type(name))                        # <class 'str'>
print(type(name1))                       # <class 'tuple'>

# access through index
tuples=("ali","ahmad","hassan")
print(tuples[1])                         # ahmad
print(tuples[-1])                        # hassan
print(tuples[0:2])                       # ('ali', 'ahmad')

# with if
tuples=("ali","ahmad","hassan")
if "ahmad" in tuples:
    print ("yes")
else:
    print("no")                           # yes

#change the tuple
# you can not change the tuple .tuples are immutable.but you can it to conver tuple
# in to list and after that convert it in to tuple.
x=("ali","ahmad","hassan")
y=list(x)
y[1]=("numan")
print(y)                               # ['ali', 'numan', 'hassan']
print(tuple(y))                        # ('ali', 'numan', 'hassan')

# add in tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)              # ////????????????????????????????

# REMOVE FROM TUPLE
# we can not remove from tuple first we convert tuple in to list and remove item
# and than  convert it back in tuple.
x=("ali","ahmad","hassan")
z=list(x)
z.remove("ahmad")
print(z)                         # ['ali', 'hassan']
print(tuple(z))                  # ('ali', 'hassan')

# UNPACK THE TUPLE
x=("ali","ahmad","hassan")
(green,yellow,red)=x
print(green)                    # ali
print(yellow)                   # ahmad
print(red)                      # hassan

x=("ali","ahmad","hassan","rahman")
(green,yellow,*red)=x
print(green)                    # ali
print(yellow)                   # ahmad
print(red)                      # ['hassan', 'rahman']

x=("ali","ahmad","hassan","rahman")
(green,*yellow,red)=x
print(green)                    # ali
print(yellow)                   # ['ahmad', 'hassan']
print(red)                      # rahman

# USE LOOP IN TUPLE
x=("ali","ahmad","hassan","rahman")
for y in x:
    print(y)
# 2
x=("ali","ahmad","hassan","rahman")
for i in range(len(x)):
    print(x[i])
# 3
# x=("ali","ahmad","hassan","rahman")
# i=[]
# while i<len(x):
#     print(x[i])
#     i=i+1

# JOIN TWO TUPLE
a = ("a", "b" , "c")
z= (1, 2, 3)
t = a+z
print(t)                            # ('a', 'b', 'c', 1, 2, 3)

# MULTIPLY TUPLE
a = ("a", "b" , "c")
y=a*2
print(y)                           # ('a', 'b', 'c', 'a', 'b', 'c')



