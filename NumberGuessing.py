import random
import math

lower_bound = int(input("Enter Lower Bound: "))
upper_bound = int(input("Enter Upper Bound: "))

x = random.randint(lower_bound, upper_bound)
num_chances = int(math.log(upper_bound-lower_bound + 1, 2))
print("\n\t You have only ", num_chances," chances to guess the right integer.\n")

count = 0
while count < num_chances:
	guess = int(input("Enter your guess: "))
	if guess == x:
		print("You have correctly guess the integer!")
		break
	elif guess > x:
		print("You guessed too high.")
	elif guess < x:
		print("You guessed too low.")
	count += 1

if count == num_chances:
	print("\nThe correct number is %d" % x)
	print("You ran out of chances. Try again! You might have better luck!\n")
