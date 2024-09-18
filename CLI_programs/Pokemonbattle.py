#basic pokemon battle project

import random

class Pokemon:
	def __init__(self, name, hp, moves):
		self.name = name
		self.hp = hp
		self.moves = moves #can be a map of moves with dmg #

	def attack(self, move_name, opp):
		pwr = self.moves[move_name]
		print(f"{self.name} uses {move_name}!")
		opp.hp -= pwr
		print(f"{opp.name} loses {pwr} HP!")
		print(f"{opp.name} has {opp.hp} HP left.")
		print()

	def faints(self):
		return self.hp <= 0


def battle(pokemon1, pokemon2):
	print(f"You have encountered a wild pokemon! It is a {pokemon2.name}!")
	print()
	while (1):
		move = random.choice(list(pokemon1.moves.keys()))
		pokemon1.attack(move, pokemon2)
		if pokemon2.faints():
			print(f"{pokemon2.name} has fainted! {pokemon1.name} wins!")
			break

		move = random.choice(list(pokemon2.moves.keys()))
		pokemon2.attack(move, pokemon1)
		if pokemon1.faints():
			print(f"{pokemon1.name} has fainted! {pokemon2.name} wins!")
			break

#pokemon dictionary
pikachu = Pokemon("Pikachu", 80, {"Thunderbolt":35, "Quick Attack":10})
charmander = Pokemon("Charmander", 120, {"Fireball":25, "Sratch":15, "Ember": 20})
squirtle = Pokemon("Squirtle", 100, {"Tackle":20, "Tail Whip":20, "Water Gun":30})


#start of game program
print("Welcome to the world of Pokemon!\n Creatures of all kinds exist in this world!\n"
	  "With them came trainers who capture and train these creatures to participate in grand tournaments!")
name = input("What is your name? ---")
print("Welcome, ", name + "!") #concatenating strings does not leave a space inbetween
starter_pokemon_list = {1:pikachu, 2:charmander, 3:squirtle}
print("Now you get to choose your starting pokemon! Courtesy of Professor Oak!")
choice = input("But you won't know which one you get! Choose from these three balls! --- ")
while (1):
	try:
		choice = int(choice)
	except ValueError:
		print("Whoops! Enter a number!")
		choice = None
		choice = input("--- ")

	if choice in starter_pokemon_list:
		my_pokemon = starter_pokemon_list[choice]
		print("You have choosen: "+ my_pokemon.name+"!")
		print()
		break
	else:
		print("Woah there! Try choosing a number from 1 to 3!")
		choice = None
		choice = input("--- ")

# random.choice needs a sequence type argument hence why we convert the dictionary view to a list
# the dict.keys() method returns a view object of the dictionary's keys; a view object allows us to see the data
# without copying it
battle(my_pokemon, starter_pokemon_list[random.choice(list(starter_pokemon_list.keys()))])
