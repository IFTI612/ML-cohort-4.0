data = [40, 30, 33 ,44] #this is called list. we can customize it like append, remove 
print(data)
data.append(45)
data.remove(30)
data.remove(33)
print(data)

##############################################################################################

dataTuple = (10 , 20) #this is called tuple. we cannot change it unless converting it to a list....
# "dataTuple.apppend(45)" will not work

# list is Mutable . Tuple is Immutable

###################################################################################################

# converting tuple to List

new_data = list(dataTuple)
new_data.append(66)
new_data.remove(10)
print(new_data)

###################################################################################################

#Dictionary "(key): value "system. Key must be unique
location= {
    ("paris" ,"France" ) :"Eiffel Tower",
    ("USA" ,"New Yourk" ) :"Statue of Liberty"
}
print(location)


person={("name"):"ifti"} #initializing dictionary
person["name"] = "Ifti Bin Islam" # updating "name" key..... 
person["age"] = 44 # adding new key to the person dictionary
del person["age"] # deleting "age" key-value pair 
print(person)