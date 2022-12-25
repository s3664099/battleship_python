# Ships
#	- Destroyer 2 squares
#	- submarine 3 squares
#	- cruiser 3 squares
#	- battleship 4 squares
#	- aircraft carrier 4 squares

#Add the code where the players fight each other - have computer vs computer

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

#Creates the board for the player and the computer
player = board.Board("Player")
computer = board.Board("Computer")

#Adds the ships to the board
player.add_ships()
computer.add_ships()

#Displays the boards
display_board.display_grid(10,player.get_grid(),computer.get_grid())