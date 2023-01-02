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


def start_game():
	#Creates the board for the player and the computer
	player = board.Board("Player")
	computer = board.Board("Computer")

	#Adds the ships to the board
	player.add_ships()
	computer.add_ships()

	#Displays the boards
	display_board.display_grid(10,player.get_grid(),computer.get_grid())

	result = 1

	#plays until somebody wins
	while result != 2:

		time.sleep(2)
		print()
		print("Computer")
		result = action.fire(player,computer)

		if result != 2:
			print("Player")
			result = action.fire(computer,player)
			print()
			if result == 2:
				print("Player has won")
		else:
			print("Computer has won")

		display_board.display_grid(10,player.get_spots_hit(),computer.get_spots_hit())

#Passes the current file as a module to the loader
if __name__ == '__main__':
	start_game()