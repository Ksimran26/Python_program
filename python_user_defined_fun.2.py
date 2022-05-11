##Arguements means it can take any no. of arguements
## Output will be in the form of Tuple.

def Student_passed(*names):

    print(names)

Student_passed("Dhoni")
Student_passed("Kohli","Sachin")


##a**args means data with keys
##output willl be in the form of dictionary

def Student_passed(**names):

    print(names)

Student_passed(name = "Kohli")
Student_passed(name = "Dhoni",age = 33)


##In the given program Return is last executable function
def Student_Mark(eng,math,student_name):

    total = eng + math
    return total

print(Student_Mark(40,50,"dhoni"))



##Scoping

var = 100 #outside variable(Global)
def fun():
    var = 10 #local variable
    print(var)

print(var)
fun()
print(var)


var = 100 #outside variable(Global)
def fun():
    var = 10 #local variable
    print(var)

print(var)
fun()
print(var)

##counter stops at 100th time

counter = 0
def fun():
    global counter
    print("hello",counter)
    counter = counter + 1
    if counter == 100:
        return
    fun()
fun()

counter = 0
def fun():
    global counter
    print("hello",counter)
    counter = counter + 1
    while counter < 101:
       fun()
fun()


counter = 0
def fun():
    global counter
    print("hello",counter)
    counter = counter + 1
    if counter < 101:
       fun()
fun()








































