#build a grid of 10x10
#Populate the grid with the ships
#	- Destroyer 2 squares
#	- submarine 3 squares
#	- cruiser 3 squares
#	- battleship 4 squares
#	- aircraft carrier 4 squares

def build_grid(rows):

	row = []
	for i in range(rows):
		col = []
		for j in range(rows):
			col.append(".")
		row.append(col)
	return row

def create_line(lines):

	for x in range(21):
		lines = "{}-".format(lines)

	return lines

def display_line(line, user, spaces,x):

	for y in range(10):
		line = "{}|{}".format(line,player[x][y])

	line = "{}|".format(line)

	return line

def display_grid(rows,player,computer):

	lines = ""
	spaces = "             "

	lines = create_line(spaces)
	lines = create_line("{}{}".format(lines,spaces))

	print(lines)

	for x in range(10):

		line = spaces
		line = "{}{}".format(display_line(line,player,spaces,x),spaces)
		line = "{}|".format(display_line(line,computer,spaces,x))
	
		print(line)
		print(lines)

rows = 10
player = build_grid(rows)
computer = build_grid(rows)
display_grid(rows,player,computer)






