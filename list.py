marks = [65,89,67]
print(marks)
print("Lenght: ",len(marks))
print(marks[0]) # 0 positin value
print(marks[-1]) # -1 positin value (count from right side)
print(marks[0:2]) # 2 position value not print (only 0,1 vlaue print)
print(marks[0:1]) # 1 position value not print

#for in list
print("")
for i in marks:
    print(i)

print("")
marks.append(77) #aad value
print(marks)

print("")
marks.insert(1,69) #add value in position
print(marks)

print("")
#exist or not
print(99 in marks)
print(69 in marks)

print("")
#lenght
print("lenght : ",len(marks))

print("")
#while loop
i=0
while i<len(marks):
    print(marks[i])
    i+=1

print("")
#clear
marks.clear()
print(marks)