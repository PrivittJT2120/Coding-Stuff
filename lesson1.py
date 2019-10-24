# Calculations, printing, variables

# Printing to the screen
# The built in function print(), prints to the screen
# It will print both Strings and numbers
print("Printing to the screen")
print("hello") #a string
print('hello again')
print(6) # a number
print("6") # a string again
print(6 + 6) # 12
print("6" + "6") # string concatenation
# print("6" + 6) # What will this do? -> error.

# performing Calculations
# addition +
# subtraction -
# multiplication *
# division /
# exponents **
# modulo %
print(4 - 2) # Subtraction = 2
print(4 * 2) # multiplication = 8
print(4 / 3) # Division 1.333...
print(4 ** 3) #exponents = 64
print("Modulo operator test...")
print(5 % 3)
print(10 % 2)
print(16 % 3)
# Modulo gives remainders
# python operators follow the same order of operation as Math. (PEMDAS)
print(4 - 2 * 2) # should give zero
print((4-2) * 2) # should give 4

# Variables
# variables are used to hold data
# variables are declared and set to a value (initializing)
badLuck = 13 # declared a variable called badLuck and initialized it to 13
# i can print the variable using it's name
# print("badLuck = " + badLuck) # causes an error
print("badLuck = " + str(badLuck)) # cast it to a string
goodLuck = "4" # String variable
print("goodLuck = " + goodLuck) # don't have to cast it because it is already a string
badLuck + 5 # this is pointless
print(badLuck)
badLuck = badLuck + 5 # badLuck is now 18
print(badLuck)

# you can also save input into variables
# using input(), A prompt goes inside the ()
name = input("What is your name? ")
print("Hello" + name)
print(name * 10)
name = name + "\n" # escape character (newline)
print(name * 10)
# let's try some math
base = input("Enter the base number: ")
exp = input("Enter the exponent: ")
print(int(base) ** int(exp))