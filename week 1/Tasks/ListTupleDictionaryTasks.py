#Task 1 for list
numbers = [20,30,33,40,43]
numbers.append(49)
numbers.remove(numbers[1])

ListSum = 0

for x in numbers:
    ListSum = ListSum + x

print(ListSum)  

print()


#Task 2
#Creates a tuple with the names of 5 cities. Prints the third city in the tuple.
# Converts the tuple into a list, adds a new city, and converts it back to a tuple. Prints the modified tuple

cities = ("Dhaka","Barishal","Khulna","Rajshai","Rangpur")
print(cities[2])

list_cities = list(cities)
list_cities.append("Noakhali")

Tuple_cities = tuple(list_cities)
print(Tuple_cities)
print()


#task 3
# Creates a dictionary where keys are subject names (e.g., Math, Science) and values are the marks (e.g., 90, 85). 
# Adds a new subject with its mark to the dictionary. Updates the mark for one subject. Prints the average marks.

marks= {
    "math":70,
    "science":50,
    "bangla":55,
}

marks["english"] = 65
marks["bangla"] = 54

MarkSum=0
for x in marks.values():
    MarkSum = MarkSum + x

ave = MarkSum/len(marks)
print(ave)
