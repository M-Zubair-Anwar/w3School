# LOOPING
# python have two loop commands
# 1 for loop
# 2 while loop

# WHILE LOOP
i=0
while i<6:
    print(i)
    i=i+1                      # start from 1 to 5
# or
i=0
while i<6:
    print(i)
    i +=1                     # start from 0 to 5

# BREAK
i=0
while i<6:
    print(i)
    if i==4:
        break
    i +=1

# CONTINUE
i=0
while i<6:
    i += 1
    if i==3:
        continue
    print(i)

# WITH ELSE

i=0
while i<6:
    print(i)
    i +=1
else:
    print("i is no longer less than 6")

# PYTHON FOR LOOP

lit=["ali", "adal", "rehman"]
for s in lit:
    print(s)

# string looping
for a in "rahman":
    print(a)

lit=["ali","adnan", "adal", "rehman"]
for s in lit:
    print(s)
    if s=="adal":
        break                       # print 3  name

# or
lit=["ali","adnan", "adal", "rehman"]
for s in lit:
    if s =="adal":
        break
    print(s)                            # print 2 name

# continue
lit=["ali","adnan", "adal", "rehman"]
for s in lit:
    if s =="adal":
        continue
    print(s)

# RANGE
for e in range(8):
    print(e)
# or
for w in range(2,6):
    print(w)
# or
for w in range(2,12,2):
    print(w)

#else
for q in range(6):
    print(q)
else:
    print("done")
# with break
for q in range(6):
    if q==4:
        break
    print(q)
else:
    print("done")
# NESTED
lit=["ali","adnan", "adal", "rehman"]
lit1=[ "adal", "rehman"]
for q in lit:
    for w in lit1:
        print(q,w)





























