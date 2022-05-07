data = "India is History"
for X in data:
    print(X)

data = "India is History"
for X in data:
    print(X,end="")

data = "India is History"
for X in data:
    print(X,end=" ")

data = "India is History"
for X in data:
    print(X,end="*")

data = "India is History"
for X in enumerate(data):
    print(X)

data = "India is History"
for X,Y in enumerate(data):
    print(X)
    print(Y)

data = "India is History"
my_counter = 0
for x in (data):
    print(x)
    my_counter = my_counter + 1
print(my_counter)

data = "India is History"
for x in (data):
    if x == "i":
        print(x,"success")
    
    else:
        print(x,"failure")

data = "India is History"
for x in (data):
    if x == "i":
        print(x,"success")
    elif x == "s":
        print(x,"success")
    else:
        print(x,"failure")

data = "india is History"
for x in (data):
    if x == "i" or x == "s":
        print(x,"success")
    
    else:
        print(x,"failure")


data = "india is History"
for x in (data):
    if x == "i" or x == "s":
        continue
    print(x,"failure")
##It will show only failures 










