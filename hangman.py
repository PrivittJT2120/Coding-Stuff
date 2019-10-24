import time
import os
import random
turnsChoice = input("Pick your difficulty: Easy, Medium, Hard ---> ")
if turnsChoice == "Easy":
	turns = 20
	print("You have chosen easy difficulty. You are given 20 turns.")
elif turnsChoice == "Medium":
	turns = 15
	print("You have chosen medium difficulty. You are given 15 turns.")
elif turnsChoice == "Hard":
	turns = 10
	print("You have chosen hard difficulty. You are given 10 turns.")


wordBank =["france", "computer", "python", "orange", "blue", "hangman"]
cChoices = random.choice(wordBank)
myString = list(cChoices)
missedLetters = []
guessList = []
misses = 0
for letter in myString:
	guessList.append("_")
while turns > 0:
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
		if _ in guessList == 0:
			print("Congratulations! You won Hangperson. You're word was " + str(cChoices))
	else:
		print("Letter is not in the word")
		missedLetters.append(letter)
		turns = turns - 1
		misses = misses + 1
		print("Misses: " + str(misses))
		print("Incorrect Letters: " + str(missedLetters))
if turns == 0:
	print("Game Over. You lost and your word was " + str(cChoices))
else:
	print("Congratulations! You won Hangperson. You're word was " + str(cChoices))
print("Thanks for playing!")