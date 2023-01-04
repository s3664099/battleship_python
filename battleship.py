#!/usr/bin/env python3

#Add comments, and tidy code (if possible)
#An extra line is being taken when the ships are placed
#Have a check where if the value is invalid, then it is removed, and try again
#Add option for players (1 and 2) to play
#Convert to Java
#Convert to C++

import board
import display_board
import action
import time
import controller
import random


def start_game():

	turns = 0

	#Asks for the number of players
	players = controller.get_number("Please enter the number of players (0,1,2)",0,2)

	#Creates the board for the player and the computer
	opponent01 = board.Board("Deep Thought")
	opponent02 = board.Board("Marvin the Paranoid Android")

	#Checks to see how many players are playing, and will automatically generate boards based on it
	if (players == 0):
		opponent01.add_ships()
		opponent02.add_ships()
	elif (players == 1):
		opponent02.add_ships()
		controller.add_ships(opponent01,1)
	else:
		controller.add_ships(opponent01,1)
		controller.add_ships(opponent02,2)

	#Displays the boards if there are no players.
	if players == 0:
		display_board.display_grids(10,opponent01.get_grid(),opponent02.get_grid())
		time.sleep(5)

	result = 1

	#Determines who goes first
	go_first = random.randint(0,1)

	first_shot = opponent01
	second_shot = opponent02

	if (go_first == 1):
		first_shot = opponent02
		second_shot = opponent01

	print("{} goes first.".format(first_shot.get_name()))

	#plays until somebody wins
	while result != 2:

		turns += 1

		time.sleep(2)

		result = turn(second_shot,first_shot)

		if result != 2:

			if players == 2:
				display_board.display_grids(10,first_shot.get_grid(),second_shot.get_spots_hit())

			result = turn(first_shot,second_shot)

		#Sees how many players, and displays the appropriate boards
		if players == 0:
			display_board.display_grids(10,first_shot.get_spots_hit(),second_shot.get_spots_hit())
		elif players == 1:
			display_board.display_grids(10,first_shot.get_grid(),second_shot.get_spots_hit())
		else:
			display_board.display_grids(10,first_shot.get_spots_hit(),second_shot.get_grid())

		if result == 2:
			print()
			print("Game over in {} turns".format(turns))

#player takes a turn
def turn(defender,attacker):

	print("{}'s Shot".format(attacker.get_name()))

	if attacker.get_manual_player():
		result = controller.fire_shot(defender,attacker)
	else:
		result = action.fire(defender,attacker)
	print()

	#Checks for a win condition
	if result == 2:
		print("{} has won".format(attacker.get_name()))
		print()

	return result


#Passes the current file as a module to the loader
if __name__ == '__main__':
	start_game()