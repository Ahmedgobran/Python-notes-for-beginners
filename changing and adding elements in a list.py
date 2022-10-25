cars=['tesla','lambo','suzuki']
print(cars)

cars[0]="toyota"  #this way we're changing the variable assigned to the list '[0]' from tesla to toyota
print(cars)    #this is the same as reassigning normal variables but we can also do it with lists


cars.append("audi")  # the .append() function alows us to add a value to the end of the list 
print(cars)


motorcycles=[]
motorcycles.append('proton')  # we can use .append() in this case to add values to an empty list
motorcycles.append('yamaha')
print(motorcycles)
print(motorcycles[1].upper())   
# in the future the append() might be useful if we have an empty list for example and we want to add the input of the user, so we might list.append(input())


cities=[]
cities.insert(0,"cairo")   # .insert() function allows us to add a value to a specific position in the list using e.g.[0] [1] [2] etc...
cities.insert(1, "tokyo")
cities.insert(2, "dubai")
print(cities)



