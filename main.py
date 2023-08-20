# dictionaries
# dictionaries are use to save data in key and value
#a dictinaries is colletion which is odered ,changeable but not allow duplicate
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991
}
print(dic)                    # {'brand': 'fort', 'model': 'mustang', 'year': 1991}

# DICTIONARY ITEM
print(dic["brand"])         # fort
dic={
    "brand":"fort",
    "model":"mustang",
    "year":1991,
    "year":1234
}
print(dic)                   # {'brand': 'fort', 'model': 'mustang', 'year': 1234}
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


































