# Ships
#	- Destroyer 2 squares
#	- submarine 3 squares
#	- cruiser 3 squares
#	- battleship 4 squares
#	- aircraft carrier 4 squares

#Move Display functions to a separate file to support MVC patter
#Create separate file that adds ships to board
#Add check so that if there is no space for the ship, to try the other angle (unlikely)
#Make the code that adds the co-ordinates a bit more efficient

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

#Creates the lines to provide the top and bottom edges to the board - MOVE TO VIEW
def create_line(lines):

	for x in range(12):
		lines = "{}-".format(lines)

	return lines

#Displayes the lines - MOVE TO VIEW
def display_line(line, user, spaces,x):

	for y in range(10):
		line = "{}{}".format(line,user[x][y])

	line = "{}|".format(line)

	return line

#Displays the grid, side by side, for the computer and the Player - MOVE TO VIEW
def display_grid(rows,player,computer):

	lines = ""
	spaces = "             "

	lines = create_line(spaces)
	lines = create_line("{}{}".format(lines,spaces))

	for x in range(10):

		line = "{}|".format(spaces)
		line = "{}{}".format(display_line(line,player,spaces,x),spaces)
		line = "{}|".format(line)
		line = "{}".format(display_line(line,computer,spaces,x))
	
		print(line)
	print(lines)

#Creates the board for the player and the computer
player = board.Board("Player")
computer = board.Board("Computer")

#Adds the ships to the board
player.add_ships()
computer.add_ships()

#Displays the boards
display_grid(10,player.get_grid(),computer.get_grid())






