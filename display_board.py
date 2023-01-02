
#Creates the lines to provide the top and bottom edges to the board - MOVE TO VIEW
def create_line(lines):

	lines = "{} ".format(lines)
	for x in range(12):
		lines = "{}-".format(lines)

	return lines

#Displayes the lines
def display_line(line, user, spaces,x):

	for y in range(10):
		line = "{}{}".format(line,user[x][y])

	line = "{}|".format(line)

	return line

#Prints a line that displays the column numbers at the top
def create_numbers(spaces):

	numbers = "{}  ".format(spaces)

	for x in range(10):
		numbers = "{}{}".format(numbers,x)

	return numbers


#Displays the grid, side by side, for the computer and the Player - MOVE TO VIEW
def display_grids(rows,player,computer):

	lines = ""
	spaces = "             "

	lines = create_line(spaces)
	lines = create_line("{}{}".format(lines,spaces))
	number_line = "{} {}".format(create_numbers(spaces),create_numbers(spaces))

	print(number_line)
	print(lines)
	for x in range(10):

		line = "{}{}|".format(spaces,x)
		line = "{}{}".format(display_line(line,player,spaces,x),spaces)
		line = "{}{}|".format(line,x)
		line = "{}".format(display_line(line,computer,spaces,x))
	
		print(line)
	print(lines)