import copy
from random import randint

class Board:

	grid = []
	used_spots = []
	rows = 10
	object_name = ""

	def __init__(self,object_name):

		self.object_name = object_name
		self.grid = []
		self.used_spots = []

		for i in range(self.rows):
			col = []
			for j in range(self.rows):
				col.append(".")
			self.grid.append(col)

	def get_grid(self):

		return self.grid

	def add_ships(self):

		ships = [2,3,3,4,4]
		ship_code = ['a','b','c','d','e']

		code = 0

		for x in ships:
			self.grid = self.add_ship(x,ship_code[code])
			code += 1

	def add_ship(self,ship,code):

		potential_place = []
		angle = randint(0,1)

		if angle == 0:

			for x in range(9):
				for y in range(9-ship):
					used = False
					for z in range(ship):
						for i in self.used_spots:
							if (x,y+z) == i:
								used = True
					if used != True:
						potential_place.append((x,y))
		else:
			for x in range(9-ship):
				for y in range(9):
					used = False
					for z in range(ship):				
						for i in self.used_spots:
							if (x+z,y) == i:
								used = True
					if used != True:
						potential_place.append((x,y))
		
		ship_location = randint(0,len(potential_place)-1)
		ship_x = potential_place[ship_location][0]
		ship_y = potential_place[ship_location][1]

		for x in range(ship):

			self.grid[ship_x][ship_y] = code
			self.used_spots.append((ship_x,ship_y))

			if angle == 0:
				ship_y += 1
			else:
				ship_x += 1

		return self.grid



		#Get length of ship
		#Go through each of the posistions and check each of the co-ords based on the direction.
		#Compare the co-ords with the contents of used
		#If in used, then skip, otherwise add
		#Take a random position from the contents
		#Add the co-ordinates, and each around, to the used

