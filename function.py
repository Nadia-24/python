#Function is a block of code which only runs when it is called
#basic
def my_funtion():
    print("This topic is Function")
my_funtion()

#2
print("")
def fun(x):
    print(x+ "Nadia")
fun("Tanjim & ")
fun("Shajia & ")

#3
print("")
def fun(y,z):
    print(y + "" + z)
fun(y="Tanjim & ", z= "Nadia")

#4
print("")
#If the number of arguments is unknown , add a * before the parameter name
def fun1(*kids):
    print("The youngest child is "+ kids[1]+".")
fun1("Nadia","Moon","x")

#5
print("")
def fun2(country="Bangladesh"):
    print("I am from "+country)
fun2("Spain")
fun2("Madrid")
fun2()
fun2("India")

#6 while loop
print("")
print("while loop")
def fun3(x):
    while x<10:
        print(x+2)
        x+=1

y= int(input("Enter a number : "))
fun3(y)

#7 for loop
print("")
print("for loop")
def fun4(z):
    for x in z:
     print(x * 2)
y=[1,3,9,8]
fun4(y)

#8 return value
print("")
print("Return value")
def fun5(x):
    return 5*x
print(fun5(3))
print(fun5(9))





