import random
import math
import nltk
from nltk.corpus import words

nltk.download('words')

word_list = words.words()


print("Welcome! This is a game where you guess the word one character at a time.\n")
name = input("Firstly, what is your name? Enter it here: ")
print("Good luck, ", name,"!")

word_ans = list(random.choice(word_list))
# word_ans = ["h","e","l","l","o"]
num_chances = int(math.log(len(word_list)/10 , 2))
print("Guess the characters")
word_len = len(word_ans)
word_guess = ['_'] * word_len
i = 0
tries = 0

while tries < num_chances:
	char = input("Enter a letter: ")
	if char in word_ans:
		while i < word_len:
			if word_ans[i] == char:
				word_guess[i] = word_ans[i]
			i+=1
		i = 0
		print(word_guess)
	else:
		print("That letter is not in the word")
	if '_' not in word_guess:
		print("You have guessed the word! Congratulations!")
		break
	tries+=1
if tries == num_chances:
	print("The correct word was: ", ''.join(word_ans))
	print("Sorry. You ran out of tries. Better luck next time!")
