# FUNCTION
# A functions is block of code which is only run when it is called.
# you can pass data known as parameters in to funtion .a function
# can return data as a result.
def fun ():
    print("hello")
fun()                                  # hello

# ARGUMENR
def name(sname):
    print(sname,"cricketer")
name("ali")                             # ali cricketer
name("adal")                            # adal cricketer
name("hassn")                           # hassn cricketer

def nam(name,lname):
    print(name+" "+lname)
nam("jone","cris")           # jone cris

# * ARGS
def boy(*name):
    print("the youngest child is" + name[1])
boy("ali","ahsan","rehan",)

def boy(ch1,ch2,ch3):
    print("the youngest child is"+" " + ch3)
boy(ch1 = "ali",ch2="ahsan",ch3="rehan",)


def boy(**name):
    print("the youngest child is" + name["lname"])
boy(fname="ali",lname= " dogar")

# DEFALT PERAMETER VALUE
def location(country="pakistan"):
    print("i am from "+ country)
location("sweden")
location("turky")
location("usa")
location()

def list(food):
    for s in food:
        print(s)
friuts=["apple","banana","orange"]
list(friuts)

# RETURN
def count(x):
    return 5*x
print(count(3))










































