# dictionaries
# dictionaries are use to save data in key and value
#a dictinaries is colletion which is odered ,changeable
# but not allow duplicate
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991
}
print(dic)              # {'brand': 'fort', 'model': 'mustang', 'year': 1991}

# DICTIONARY ITEM
print(dic["brand"])         # fort
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
print(dic)             # {'brand': 'fort', 'model': 'mustang', 'year': 1234}
print(len(dic))              # 3
print(type(dic))             # <class 'dict'>

# CONSTRUCTOR
name=dict(name = "John", age = 36, country = "Norway")
print(name)                 # {'name': 'John', 'age': 36, 'country': 'Norway'}

# accessing
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
x=dic["model"]
print(x)                      # mustang
# OR
y=dic.get("medel")            # mustang
# get key
z=dic.keys()
print(z)                       # dict_keys(['brand', 'model', 'year'])

# ADD KEY
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
d=dic.keys()
print(d)                               # dict_keys(['brand', 'model', 'year'])
dic["color"]= "white"

print(d)                    # dict_keys(['brand', 'model', 'year', 'color'])

# VALUE
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
f=dic.values()
print(f)                     # dict_values(['fort', 'mustang', 1234])


dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
g=dic.values()
print(g)                             # dict_values(['fort', 'mustang', 1234])
dic["expire"]="2003"
print(g)                     # dict_values(['fort', 'mustang', 1234, '2003'])

# GET ITEMS
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
g=dic.items()
print(g)#dict_items([('brand', 'fort'), ('model', 'mustang'), ('year', 1234)])

# IF IN DICTIONARIES
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
if "brand" in dic:
    print("fort")                      # fort

# CHANGE DIC ITEM

dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}

dic["year"]=2003
print(dic)          # {'brand': 'fort', 'model': 'mustang', 'year': 2003}
# 2nd way
dic.update({"year":2004})
print(dic)         # {'brand': 'fort', 'model': 'mustang', 'year': 2004}

# REMOVING ITEMS
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
dic.pop("model")
print(dic)            # {'brand': 'fort', 'year': 1991}

dic.popitem()
print(dic)            # {'brand': 'fort'}

dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
del dic ["model"]
print(dic)           # {'brand': 'fort', 'year': 1991}

dic.clear()
print(dic)            # {}

# FOR LOOP OF KEYS
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for w in dic:
    print(w)
# 2nd way
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for w in dic.keys():
    print(w)

# FOR LOOP OF VALUE
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for w in dic:
    print(dic[w])
# 2ND WAY
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for w in dic.values():
    print(w)

# LOOPING BOTH KEY AND VALUE
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for a,s in dic.items():
    print(a,s)
# 2nd way
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
for a in dic.items():
    print(a)

# COPY DIC
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
E=dic.copy()
print(E)
# 2ND WAY
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
f=dict(dic)
print(f)

# TWO OR MORE DICTIONARIES IN ONE DICTIONARIES
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
}
dic2={
    "brand":"fort",
    "model":"mustang",
    "year":199,
}
dic3={
    "child1":dic,
     "child2":dic2
}
print(dic3)

# find value in dic3
print(dic3["child2"]["year"])
















