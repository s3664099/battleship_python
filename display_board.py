
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