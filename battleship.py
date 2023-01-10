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

board_size = 10

def start_game():

	skip_turn = False

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

	show_grid(board_size,first_shot,second_shot,players)

	#plays until somebody wins
	while result != 2:

		turns += 1

		time.sleep(2)

		result,skip_turn = turn(second_shot,first_shot,skip_turn)

		#Checks if two players are playing and the board will need to be displayed every time
		#A player takes a turn
		if result != 3:

			if players == 2:
				display_board.display_grids(10,first_shot.get_grid(),second_shot.get_spots_hit())

			result,skip_turn = turn(first_shot,second_shot,skip_turn)

		show_grid(board_size,first_shot,second_shot,players)

		if result == 3:
			print()
			print("Game over in {} turns".format(turns))

#Displays the board
def show_grid(board_size,first_shot,second_shot,players):

	#Sees how many players, and displays the appropriate boards
	if players == 0:
		display_board.display_grids(board_size,first_shot.get_spots_hit(),second_shot.get_spots_hit())
	elif players == 1:

		if first_shot.get_manual_player():
			display_board.display_grids(board_size,first_shot.get_grid(),second_shot.get_spots_hit())
		else:
			display_board.display_grids(board_size,first_shot.get_spots_hit(),second_shot.get_grid())
	else:
		display_board.display_grids(board_size,first_shot.get_spots_hit(),second_shot.get_grid())

#player takes a turn
def turn(defender,attacker,skip_turn):

	result = 0

	if skip_turn == False:

		print("{}'s Shot".format(attacker.get_name()))

		#Checks whether a manual player or not, and if not calls the algorithm
		if attacker.get_manual_player():
			result = controller.fire_shot(defender,attacker)
		else:
			result = action.fire(defender,attacker)
		print()

	skip_turn = False

	if result != 0:
		skip_turn = True

	#Checks for a win condition
	if result == 3:
		print("{} has won".format(attacker.get_name()))
		print()

	return result,skip_turn


#Passes the current file as a module to the loader
if __name__ == '__main__':
	start_game()