# Ships
#	- Destroyer 2 squares
#	- submarine 3 squares
#	- cruiser 3 squares
#	- battleship 4 squares
#	- aircraft carrier 4 squares

#Add comments, and tidy code (if possible)
#An extra line is being taken when the ships are placed
#Have a check where if the value is invalid, then it is removed, and try again
#Add option for players (1 and 2) to play
#Convert to Java
#Convert to C++

#Algorithm
# - Select Random spot
# - Remove spot from list of spots
# - If miss, try again
# - If hit - creates a new list of immediate co-ordinates
# - Next if missed try another
# - If hit - remove sides, and only before and after.
# - If ship sank, remove all co-ordinates around ship from spots
# - If not, try again

import board
import display_board
import action
import time

#Creates the board for the player and the computer
player = board.Board("Player")
computer = board.Board("Computer")

#Adds the ships to the board
player.add_ships()
computer.add_ships()

#Displays the boards
display_board.display_grid(10,player.get_grid(),computer.get_grid())

for x in range(20):

	time.sleep(2)
	print()
	print("Computer")
	action.fire(player,computer)
	print("Player")
	action.fire(computer,player)
	print()
	display_board.display_grid(10,player.get_spots_hit(),computer.get_spots_hit())
