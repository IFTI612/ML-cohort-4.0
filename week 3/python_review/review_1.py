import math

#1/ write a program to print 'Twinkle Twinkle Little Star' poem in python
print("Twinkle Twinkle, Little Star")
print("How I wonder what you are")
print("Up above the world so high")
print("Like a dimond in the sky")
print()
#2/ write a python program to find remainder when a number 'x' taken from user input is divided by another number 'y' which is also taken from user input

x = int(input("Enter X_"))
y = int(input("Enter Y_"))
z = x%y

print(f"remainder is__{z}")

#3/ write a python program to find average of 'n' numbers taken from user input

user_in = int(input("Enter number of inputs___"))

sum = 0
for x in range(0,user_in):
    y = float(input())
    sum = sum + y

ave = sum /user_in
print(f"Average is___{ave}")

#4/ write a python program to find to find the square root and squared value of x taken from user input

x = float(input("Give me a number for square root___"))
squre_root = math.sqrt(x)

print(squre_root)

#5/ write a program to detect if there are double spaces in a string and replace the double space with a single space

sentence = 'hi  how are you?'

 
print(sentence.replace('  ',' '))
print()

#6/ write a program to store seven fruits in a list entered by the user

fruits = []
n = int(input("Enter the number of fruits___"))

for x in range(0,n):
    fruits.append(input())

print("You have stored__",fruits)  
print()

#7/ write a program to accept marks of 6 students and display them in a sorted manner and find out their average

marks = [30,20,40,50,70,10]

marks.sort()
print(marks)

sum = 0

for x in marks:
    sum = sum +x
ave = sum /6 

print(f"The average marks is {ave}")
print()

#8/ write a python program to count the number of zeros in a list, L=[1,0,0,1,0,0,2,0,3,-5,0,0]

L=[1,0,0,1,0,0,2,0,3,-5,0,0]

count = 0
for x in L:
    if(x==0):
        count= count +1

print(f"the number of zeros in list L is {count}")
print()


#9/ write a program to take user input of 8 numbers and count the unique numbers

marks=[]

print("input 8 numbers____")
for x in range(0,8):
    marks.append(input())

print("before____")
print(marks)
marks = list(dict.fromkeys(marks))    
print("after____")
print(marks)

#10/ create an empty dictionary, allow 4 friends to enter their favourite programming language as values and keys as their name. and display them. assume the names are unique

frinds = {}

no_fri = 4

for x in range(0,no_fri):
    name = input(f"{x+1}/ name of your friend__")
    pLanguage = input(f"{name}'s favorite programming language is __")
    frinds[name]=pLanguage

print(frinds)    