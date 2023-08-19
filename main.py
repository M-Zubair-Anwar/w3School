# operator and list
# operator are used to perfome operations on variable and  values.
# exp
print(10+3)                                # 13

#1 Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# lists
# lists are use to store multiple item in a single variable.
# lists are created to use square bracket.list items are ordered,changeable and allow
# to duplicate.
list=["apple","banana","cherry','apple"]
print(list)                                   # ['apple', 'banana', "cherry','apple"]
print(len(list))                              # 3
print(type(list))                             # <class 'list'>
# for index
print(list[1])                                # banana
print(list[-1])                               # cherry','apple
# for range
print(list[2:3])                               # ["cherry','apple"]
print(list[-1:-3])                             # []
print(list[:3])                                # ['apple', 'banana', "cherry','apple"
print(list[2:])                                # ["cherry','apple"]
# check if item is exists
list=["apple","banana","cherry','apple"]
if "apple" in  list:
    print("yes")                                # yes
# change the item
list=["apple","banana","cherry','apple"]
list[1]="mango"
print(list)                                     # ['apple', 'mango', "cherry','apple"]

list=["apple","banana","cherry"]
list[1:2]=["mango","watermelon"]
print(list)                              #['apple', 'mango', 'watermelon', 'cherry']

list.insert(2,"grapes")
print(list)                      #['apple', 'mango', 'grapes', 'watermelon', 'cherry']

list.append("orange")
print(list)       #['apple', 'mango', 'grapes', 'watermelon', 'cherry', 'orange']

# extend list
fruits=["apple","banan","orange"]
vagetale=["okra","spinach"]
fruits.extend(vagetale)
print(fruits)              #['apple', 'banan', 'orange', 'okra', 'spinach']

# remove
fruits.remove("apple")
print(fruits)               #['banan', 'orange', 'okra', 'spinach']

# remove specific in index
# if you do not mention the index than pop remove the last item.
fruits.pop(1)
print(fruits)              #['banan', 'okra', 'spinach']

# delete list
m=[1,3,4]
del m
# # celar list
# m.clear()
# print(m)

# looping a list
lis=["apple","orange","banana"]
for t in lis:
    print(t)
#
# # looping through
li=["mango","apple","orange","banana"]
for i in range(len(li)):
    print(li[i])

# looping through while loop
l=["mango","apple","orange","banana"]
i=0
while i<len(l):
    print(l[i])
    i=i+1

# looping using the list comprehension
lists=["man","app","ora","ban"]
[print(x) for x in lists]

list1=["man","app","ora","ban"]
list2=[]
for x in list1:
    if "n" in x:
        list2.append(x)
print(list2)                               # [ 'man', 'ban']

# short method
list3=["man","app","ora","ban"]
list4=[x for x in list3 if "m" in x]
print(list4)                               #  ['man']
# other example
list5=[x for x in list3 if x != "man" ]
print(list5)                                # ['app', 'ora', 'ban']
# in thie example x not accept man in list

list3=["man","app","ora","ba"]
newlist=[x for x in list3]
print(newlist)                             # ['man', 'app', 'ora', 'ba']

# iterable
# you can create iterable using rang function
nlist=[x for x in range(10)]
print(nlist)                              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nlist=[x for x in range(10) if x<5]
print(nlist)                             # [0, 1, 2, 3, 4]

# for upper case
list3=["man","app","ora","ba"]
nlist=[x.upper() for x  in list3]
print(nlist)                             #['MAN', 'APP', 'ORA', 'BA']

#print hello to all value
list3=["man","app","ora","ba"]
nl=["hello" for x in list3]
print(nl)                              #['hello', 'hello', 'hello', 'hello']

# replace the item
list3=["man","app","ora","ba"]
nlist=[x if x != "app" else "nan" for x in list3 ]
print(nlist)                            #['man', 'nan', 'ora', 'ba']

# sort a list
# sort a list by alphanumerically.asending
# if in list capital leter accure than sort case insensitive and result not sort
list3=["man","app","ora","ba"]
list3.sort()
print(list3)                           #['app', 'ba', 'man', 'ora']

# sort descending oder
list3=["man","app","ora","ba"]
list3.sort(reverse=True)
print(list3)                          #['ora', 'man', 'ba', 'app']

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)                            # ////?????????????????

list3=["man","app","Ora","Ba"]
list3.sort(key=str.lower)
print(list3)                               # ['app', 'Ba', 'man', 'Ora']


# reversed oder
list3=["man","app","Ora","Ba"]
list3.reverse()
print(list3)                               # ['Ba', 'Ora', 'app', 'man']

# copy list
list3=["man","app","Ora","Ba"]
li=list3.copy()
print(li)                                 # ['man', 'app', 'Ora', 'Ba']

# list3=["man","app","Ora","Ba"]
# list=list(list3)
# print(list)                               # ['man', 'app', 'Ora', 'Ba']

# join list
l1=[1,2,3,4]
l2=["a","s","d"]
l3=l1+l2
print(l3)                           # [1, 2, 3, 4, 'a', 's', 'd']

l1=[1,2,3,4]
l2=["a","s","d"]
for x in l2:
    l1.append(x)
print(l1)                          # [1, 2, 3, 4, 'a', 's', 'd']








