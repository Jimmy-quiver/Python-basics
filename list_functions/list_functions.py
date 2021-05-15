lucky_numbers = [3, 4, 5, 3, 2, 6, 3, 9, 3, 5, 3, 1, 7]
friends =["Wayne", "Legit","Intruder", "Legit", "Shiquow"]

#FUNCTIONS RELATED TO LISTS
#extend (appends a list to the end of another list)
friends.extend(lucky_numbers)
print(friends)
#append (adds another item to the end of the list)
lucky_numbers.append(8)
print(lucky_numbers)

#insert (adds an item to a specified position within the list)
friends.insert(1, "Hermit")
print(friends)

#remove (removes an item from the list)
friends.remove("Hermit")
print(friends)

#pop (removes the item from a list)
friends.pop()
print(friends)

#how to figure if a specific element is in a list. *remove the number sign at the brginning of the code in the next line*
#print(friends.index("Shiqouw"))
 # { the terminal will give you an error "ValueError: 'Shiqouw' is not in list" .This is because of the 'clear function at the end of the program }

#how to know the number of times an item is repeated)
print(friends.count("Legit"))

#how to sort a list in ascending order
lucky_numbers.sort()
print(lucky_numbers)

#how to sort a list in descending order
lucky_numbers.reverse()
print(lucky_numbers)

#how to copy a list
friends2 = friends.copy()
print(friends2)

#clear (removes all the items in a list)
friends.clear()
print(friends)
lucky_numbers.clear()
print(lucky_numbers)