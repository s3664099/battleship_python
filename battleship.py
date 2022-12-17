#build a grid of 10x10
#Populate the grid with the ships
#	- Destroyer 2 squares
#	- submarine 3 squares
#	- cruiser 3 squares
#	- battleship 4 squares
#	- aircraft carrier 4 squares

import board

def create_line(lines):

	for x in range(12):
		lines = "{}-".format(lines)

	return lines

def display_line(line, user, spaces,x):

	for y in range(10):
		line = "{}{}".format(line,user[x][y])

	line = "{}|".format(line)

	return line

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

player = board.Board("Player")
computer = board.Board("Computer")

player.add_ships()
computer.add_ships()

display_grid(10,player.get_grid(),computer.get_grid())






