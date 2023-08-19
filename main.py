# booleans
#1 booleans present on of two value ture or false
print(10>9)                      # true
print(10==9)                     # false
print(10<9)                      # false

a=122
b=100
if a>b:
    print("a is greter than b")  # if a greater than this will print
else:
    print("b is greter than a")  # otherwise this will be printed

#2 boolean ture value
print(bool(5))                   # true
print(bool("ali"))               # true
print(bool(10.2))                # true

# boolean false value
print(bool(False))               # False
print(bool(None))                # False
print(bool(0))                   # False
print(bool(''))                  # False
print(bool({}))                  # False
print(bool([]))                  # False
print(bool(()))                  # False

# example
def my_fun():
    return True
print(my_fun())                  # true

def fun():
    return False
if fun():
        print("yes")
else:
        print("no")              # no

s=100
print(isinstance(s,str))         # False
print("change")