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


