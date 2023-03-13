import display_board

#Function to get a number between a minimum and a maximum
def get_number(query,min,max):

	correct = False
	response = ""

	while not correct:

		response = input("{}: ".format(query))

		try:
			if int(response)<min or int(response) > max:
				print("Please enter a number between {} and {}".format(min,max))
			else:
				correct = True
		except:
			print("Please enter a number")

	return int(response)

def add_ships(user, num):

	ships = user.get_ships()
	user.set_manual_player()

	#Sets up the players name
	user_name = input("Select a name: ")

	if len(user_name) <1:
		user_name = "Nameless Player {}".format(num)

	user.set_name(user_name)

	for x in ships:

		potential_place = []

		display_board.display_grid(10,user.get_grid())

		print("Placing the {}".format(x.get_name()))
		length = x.get_length()
		code = x.get_letter()

		#If the angle is verticle
		ship_len_x = 0
		ship_len_y = length
		pos_x = 0
		pos_y = 1

		angle = get_angle()

		#If the angle is horizontal
		if angle == 1:
			ship_len_x = length
			ship_len_y = 0
			pos_x = 1
			pos_y = 0

		#Generates a list of potential places
		potential_place = user.select_places(ship_len_x,ship_len_y,potential_place,length,angle)

		allowable = False

		#Asks the player for a position, and checks if it is allowable
		while not allowable:
			y_pos = get_number("Enter the x position",0,9)
			x_pos = get_number("Enter the y position",0,9)

			if potential_place.count((x_pos,y_pos)) > 0:
				allowable = True
			else:
				print("You cannot place the {} there. Allowable places:".format(x.get_name()))
				list_places = []

				#Turns out the co-ords were the wrong way around, so this switches them
				for y in potential_place:
					list_places.append((y[1],y[0]))

				print(list_places)

		user.place_ship(x,x_pos,y_pos,pos_x,pos_y,length,code,angle)

	input("Press enter to continue")

#Function to retrieve player's shot manually
def fire_shot(defender,attacker):

	already_hit = False

	#Sets the win flag
	won = 0

	#Loop to prevent player for firing at the same spot more than once
	while not already_hit:

		#Gets Player's hit
		x_coord = get_number("Select Row",0,9)
		y_coord = get_number("Select Column",0,9)
		spots_hit = defender.get_spots_hit()
		grid = defender.get_grid()

		#Checks if the player has already fired there
		if grid[x_coord][y_coord] == "0":
			print("You have already fired a shot here")
		elif grid[x_coord][y_coord] == "X":
			print("You have already fired a shot here")
		elif grid[x_coord][y_coord] == ".":
			grid[x_coord][y_coord] = "0"
			spots_hit[x_coord][y_coord] = "0"
			already_hit = True
		else:
			won = 1
			grid[x_coord][y_coord] = "X"
			spots_hit[x_coord][y_coord] = "X"
			already_hit = True

			#Determines which ship has been hit, and whether it has been sunk
			ship_sunk = defender.check_ship_hit((x_coord,y_coord))

			#If sunk
			if ship_sunk != None:
				won = 2

				#Removes the ship
				defender.remove_ship(ship_sunk)

				#Checks if there are any ships left on the opponent's board
				if defender.check_remaining_ships():
					won = 3
	return won

#Function for the player to get an angle
def get_angle():

		print("Please enter the angle")
		print("0) Across")
		print("1) Down")
		return get_number("",0,1)
		









