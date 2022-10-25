names=['ahmed','ali','mohamed','rico']
print(names)

del names[2]   # del function deletes the nth element from our list (e.g. del variable[1] which will delete the second item in the list)
print(names)


last_name= names.pop()   #. pop() function removes last element from a list and returns its value
print(last_name)
print(names)

print(f"the last name in the list is {last_name.title()}")

first_name= names.pop(0) #we can also put a number in the .pop() e.g. .pop(0) to specify which element in the list we want to remove in this case it will be the first elemnt

print(f"the first name in the list is {first_name.title()}")
