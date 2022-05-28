var = {}
print(type(var))

var = {"name":"dhoni","team":"csk"}
var1 = {"age":33}
var2 = {"lan":"eng"}
output = {**var,**var1,**var2}
print(output)
print(type(var))

##Dictioanry is mutable.
var = {"name":"dhoni",9:33,98.9:"arjun",("a","B"):"veena",True:"rahul"}
var["name"] = "Kohli"
print(var)
print(type(var))
