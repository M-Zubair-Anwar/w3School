# set
#set are used to store multiple items in on variable .
# a set is colletion which is unordered.unchangeable and unindexed
# every time it print defferent result
# ture and one is consider the same
set={"ali","header","rahman"}
print(set)                             # {'rahman', 'header', 'ali'}

# dulicate not allowed
name={"ali","header","rahman","ali"}
print(name)                            # {'ali', 'header', 'rahman'}
print(len(name))                       # 3
print(type(name))                      # <class 'set'>

# na=set(("ali","header","rahman","ali"))
# print(na)                            ??????????  not run pycham

# LOOP IN SET
name={"ali","header","rahman","ali"}
for x in name:
    print(x)

# value accurance
name={"ali","header","rahman","ali"}
for x in name:
    if "ali" in x:
        print("yes")                       # yes
    # else:
    #     print("na")
# 2nd way
print("ali" in name)                       # True

# ADD METHOD
name={"ali","header","rahman","ali"}
name.add("sohan")
print(name)                               # {'sohan', 'header', 'ali', 'rahman'}
# 2 SET ADD
name={"ali","header","rahman","ali"}
num={"mudassar","raja"}
num.update(name)
print(num)                        # {'rahman', 'raja', 'header', 'ali', 'mudassar'}

# REMOVE SET ITEM
name={"ali","header","rahman","adal"}
name.remove("rahman")
print(name)                                  # {'ali', 'header', 'adal'}

name={"ali","header","rahman","adal"}
name.discard("header")
print(name)                                  # {'ali', 'rahman', 'adal'}

# pop method reove a random item
name={"ali","header","rahman","adal"}
name.pop()
print(name)                                  # {'ali', 'rahman', 'header'}

# clear method empties the set
name={"ali","header","rahman","adal"}
name.clear()
print(name)                                  # set()

# delete
# name={"ali","header","rahman","adal"}
# del name
# print(name)                                  # this will raise error

# JOIN SET
name={"ali","header","rahman","ali"}
num={"mudassar","raja"}
n3=name.union(num)
print(n3)                     #{'ali', 'rahman', 'mudassar', 'raja', 'header'}

# duplicates
x={"ali","header","rahman","ali"}
y={"mudassar","raja","ali"}
x.intersection_update(y)
print(x)                                      # {'ali'}

x={"mudassar","header","rahman","ali"}
y={"mudassar","raja","ali"}
z=x.intersection(y)
print(z)                                     # {'mudassar', 'ali'}

# KEP ALL BUT NOT DUBLICATE
x={"mudassar","header","rahman","ali"}
y={"mudassar","raja","ali"}
x.symmetric_difference_update(y)
print(x)                                   # {'header', 'raja', 'rahman'}

x={"mudassar","header","rahman","ali"}
y={"mudassar","raja","ali"}
z=x.symmetric_difference(y)
print(z)                                    # {'raja', 'header', 'rahman'}













