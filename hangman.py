import time
import random
turnsChoice = input("Pick your difficulty: Easy, Medium, Hard ---> ")
if turnsChoice == "Easy":
	turns = 20
	print("You have chosen easy difficulty. You only have 20 misses.")
elif turnsChoice == "Medium":
	turns = 15
	print("You have chosen medium difficulty. You only have 15 misses.")
elif turnsChoice == "Hard":
	turns = 10
	print("You have chosen hard difficulty. You only have 10 misses.")
wordBank =["france", "computer", "python", "orange", "blue", "hangman", "movie", "program",
 "halloween", "coding", "window", "competition", "random", "creation", "evening", "morning", 
 "afternoon", "principal", "verrado"]
cChoices = random.choice(wordBank)
myString = list(cChoices)
missedLetters = []
guessList = []
misses = 0
for letter in myString:
	guessList.append("_")
while turns > 0:
	print(guessList)
	letter = input("Guess a letter: ")
	if letter in cChoices:
		print("Letter is in word")
		count = 0
		for l in myString:
			if l == letter:
				guessList[count] = l
			count = count + 1
		print(guessList)
		print("Incorrect Letters: " + str(missedLetters))
		if not '_' in guessList:
			print("Congratulations! You won Hangperson. You're word was " + str(cChoices))
			print("Misses: " + str(misses))
			break
	else:
		print("Letter is not in the word")
		if letter not in missedLetters:
			missedLetters.append(letter)
		turns = turns - 1
		misses = misses + 1
		print("Misses: " + str(misses))
		print("Incorrect Letters: " + str(missedLetters))
if turns == 0:
	print("Game Over. You lost and your word was " + str(cChoices))
	print("Misses: " + str(misses))

print("Thanks for playing!")
