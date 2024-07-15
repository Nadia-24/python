print("Age Check for vote")
x = int(input("Enter age : "))
print("My age is ",x)

if x>=18:
    print("So, you can vote")
elif x<18 and x>4:
    print("You can't vote")
else:
    print("You are child")

print("")

#Mini calculater
print("Mini Calculator")
F = int(input("Enter 1st number: "))
O = input("enter operator(+,-,*,**,/,%): ")
S = int(input("Enter 2nd numner: "))

if O=='+':
    print(F+S)
elif O=='-':
    print(F-S)
elif O=='*':
    print(F*S)
elif O=='**':
    print(F**S)
elif O=='/':
    print(F/S)
elif O=='%':
    print(F%S)    
else:
    print("")

