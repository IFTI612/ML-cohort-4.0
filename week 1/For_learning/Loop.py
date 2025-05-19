
fol = ["apple","mango","orange","banana"] #list

for x in fol:
    print(x)

print()
for x in range(10):           #DONT FORGET ABOUT " : " <- THIS THING
    print(x)  

print()
number = 1
for x in range(3):
    for y in range(3): #inner loop, "Indentation must be use in very careful way"
        print(number,end=" ")
        number+=1
    print()         