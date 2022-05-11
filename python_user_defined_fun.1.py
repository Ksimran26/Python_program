print("hello")
print("welcome to my programming")

## Function without arguement or signature or parameter.

def My_Fun():
      
      print("hello")
      print("welcome to my programming")

My_Fun() #Function is calling

## Function definition with arguement or signature or parameter

def My_Fun(name) :
      
     print("hello",name)
     print("welcome to my programming")
     
My_Fun("dhoni")
My_Fun("kohli")

## Function with keyword Arguements:
     
def My_Fun(name,country):
    if isinstance(name,str):
        if isinstance(country,str):
            print("hello",name,"from",country)
            print("welcome to my programming")

My_Fun("dhoni","india")  #Function calling
My_Fun("kohli","banglore")

## Function Definition with Default Arguement

def My_Fun(name,country="India"):
    print("hello",name,"from",country)
    print("welcome to my programming")
My_Fun("kohli")
My_Fun("ricky","australia")

def My_Fun(name="sachin",country=None):#fubction definition with default arguement or signature or parameter

    print("hello",name,"from",country)
    print("welcome to my programming")

My_Fun("kohli")
My_Fun("ricky","australia")









