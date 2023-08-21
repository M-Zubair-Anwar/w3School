# if else
# example
a=101
b=12
if a >b:
    print("a is greater")               # a is greater

# ELIF
a=12
b=12
if a >b:
    print("a is greater")
elif a==b:
    print("a and b equal")                  # a and b equal

# ELSE
a=10
b=12
if a >b:
    print("a is greater")
elif a==b:
    print("a and b equal")
else:
    print("b is greter")                    # b is greter
# 2nd way
a=1
b=12
if a >b:
    print("a is greater")
else:
    print("nothing")                       # nothing

# SHORT METHOD
a=111
b=12
if a>b: print("select a")               # select a

q=111
w=122
print("q") if q>w  else  print("w")     # w
print("y") if q>w else print("n") if w>q else print("yn")    # n

# AND
a=1111
s=122
d=111
if a>s and s>d:
    print("in both codition")   # in both codition
# OR
a=1111
s=1222
d=111
if a>s or s>d:
    print("in one codition")    # in one codition

# NOT
a=12
b=23
if not a>b:
    print("a is not greater than b")  # a is not greater than b
# NESTED IF
a=122
b=23
if a>b:
    print("a is greater")             # a is greater
    if b<a:
        print("b is lesser")          # b is lesser
    else:
        print("nothing")

# PASS
a=122
b=232
if a>b:
    pass


