import copy
import ship
from random import randint

#Creates an object named board
class Board:

	grid = []
	used_spots = []
	rows = 10
	object_name = ""
	ships = []

	def __init__(self,object_name):

		#Clears the variables
		self.object_name = object_name
		self.grid = []
		self.used_spots = []
		self.ships = []

		#Builds the grid
		for i in range(self.rows):
			col = []
			for j in range(self.rows):
				col.append(".")
			self.grid.append(col)

	#Returns the Grid
	def get_grid(self):

		return self.grid

	#Adds the ships to the board
	def add_ships(self):

		#Builds the Ships
		self.ships.append(ship.ship(2,'a','destroyer'))
		self.ships.append(ship.ship(3,'b','submarine'))
		self.ships.append(ship.ship(3,'c','cruiser'))
		self.ships.append(ship.ship(4,'d','battleship'))
		self.ships.append(ship.ship(4,'e','aircraft carrier'))

		code = 0

		#Goes through each of the ships and adds them to the board
		for x in self.ships:
			print("{} {} {}".format(x.get_name(),x.get_length(),x.get_letter()))
			self.grid = self.add_ship(x.get_length(),x.get_letter())
			code += 1

	#Adds the ship
	def add_ship(self,ship,code):

		#Creates a list to hold the potential positions the ships can take
		potential_place = []

		#Selects an angle for the ship
		angle = randint(0,1)

		#The Angle is Vertical
		if angle == 0:

			#Goes across the board and checks the positions the ship will occupy to see if it is valid
			for x in range(9):
				for y in range(9-ship):
					used = False
					for z in range(ship):

						#If the there is a space next to a ship, the position is not valid
						for i in self.used_spots:
							if (x,y+z) == i:
								used = True

					#Otherwise the space is a potential space and is added to the list
					if used != True:
						potential_place.append((x,y))

		#If the Angle is Horizontal
		else:

			#Goes across the board and checks the positions the ship will occupy to see if it is valid
			for x in range(9-ship):
				for y in range(9):
					used = False
					for z in range(ship):

						#If the there is a space next to a ship, the position is not valid				
						for i in self.used_spots:
							if (x+z,y) == i:
								used = True

					#Otherwise the space is a potential space and is added to the list
					if used != True:
						potential_place.append((x,y))
		
		#A random position is selected for the ship
		ship_location = randint(0,len(potential_place)-1)
		ship_x = potential_place[ship_location][0]
		ship_y = potential_place[ship_location][1]

		#The spaces occupied, and the surrounding spaces are added to a list of used spaces
		for x in range(ship):

			self.grid[ship_x][ship_y] = code
			self.used_spots.append((ship_x,ship_y))
			self.used_spots.append((ship_x+1,ship_y+1))
			self.used_spots.append((ship_x+1,ship_y))
			self.used_spots.append((ship_x+1,ship_y-1))
			self.used_spots.append((ship_x-1,ship_y+1))
			self.used_spots.append((ship_x-1,ship_y))
			self.used_spots.append((ship_x-1,ship_y-1))
			self.used_spots.append((ship_x,ship_y+1))
			self.used_spots.append((ship_x,ship_y-1))

			#Moves to the next space
			if angle == 0:
				ship_y += 1
			else:
				ship_x += 1

		return self.grid
