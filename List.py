favFoods = ["Frenchtoast", "Chicken Alfredo", "Hotdogs"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# Adds to the end of the list
favFoods.append("French Fries")
print(favFoods)
print("My fourth favorite food is " + favFoods[3])
# insert - Adds to an index in a list
favFoods.insert(1, "Chicken")
print(favFoods)
# Remove an item from the list
favFoods.remove("Chicken")
print(favFoods)
# Remove by index
favFoods.pop(2)
print(favFoods)
favFoods.insert(4, "Hotdogs")
 # Loops through the list
for food in favFoods:
 	print(food)

numList = [5, 3, 9, 10, 4, 30, 25, 64]

# Loop through the list and add all the numbers together then print the sum

sum = 0
for num in numList:
	sum = sum + num

print(sum)
# Function to get the length of the list
print(len(numList))

# make a list for favorite movies
# prompt for a favorite movie
# example
myFood = input("What is your favorite food? ")
favFoods.append(myFood)
print(favFoods)

myMovie = ["Ready Player One", "Avengers Engame", "Polar Express", "The Iron Giant", "Spirit"]
myMov = input("What is your favorite movie? ")
myMovie.append(myMov)
print(myMovie)

# List methods and functions
# append - adds an item to the end of a list
# insert - adds an item to a specific index
# Remove - removes a specified item from a list
# pop - removes an item from a specified index
# len - returns the length of a list
print(favFoods[len(favFoods)-1])