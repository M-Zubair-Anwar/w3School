# python intro first code
print("hello worlds!")
# creating a comments .these comment ignore by python.
# 2.variable are container for storing data value
# it my by integer,string,floating
y=5               # integer value
name="ali"        # string value
z=10.0            # floating value
print(y)          # result is 5
print(name)       # result is ali
print(z)          # result is 10.0

a,b,c="orange","banana","cherry"
print(a)         # result is orange
print(b)         # result is banana
print(c)         # result is cherry

fruits=["apple","banana","cherry"]
a,b,c=fruits
print(a)        # result is orange
print(b)        # result is banana
print(c)        # result is cherry
# global variable created outside of funtion and can  use both side
# (inside and outside) of funtion and other side local variable declared in
# funtion
x="ali"
def name():
    x="ahmad"
    print("my name is",x)
name()                      # result is my name is ahmad
print("my name is",x)       # result is my name is ali