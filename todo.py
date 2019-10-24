print("Hello and welcome to the ToDo list machine.")
# Make a variable to hold your list
todoList = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	task = 0
	choice = input("What do you wish to do? ")

	if choice == "q":
		break
	elif choice == "a":
		listAdd = input("What task would you like to add right now? ")
		todoList.append(listAdd)
		print("Cool, we'll add " + str(listAdd) + " to your list of tasks.")
	elif choice == "r":
		listRem = input("What task have you completed or want to remove from your list? ")
		todoList.remove(listRem)
	elif choice == "p":
		print("Here is your wonderful list of things to do. Have fun!")
		for todo in todoList:
			task = task + 1
			print("Task " + str(task) + " " + str(todo))
	else:
		print("You suck with directions don't ya buddy. Please enter a legit option.")

