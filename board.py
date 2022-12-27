import copy
import ship
from random import randint

#Creates an object named board
class Board:

	grid = []
	spots_hit = []
	used_spots = []
	rows = 10
	object_name = ""
	ships = []
	grid_size = 9
	potential_shots = []
	ship_shots = []
	hit_ship = False

	def __init__(self,object_name):

		#Clears the variables
		self.object_name = object_name
		self.grid = []
		self.used_spots = []
		self.ships = []
		self.grid_size = 9
		self.potential_shots = []
		self.ship_shots = []
		self.hit_ship = False

		#Builds the grid
		for i in range(self.rows):
			col = []
			for j in range(self.rows):
				col.append(".")
			self.grid.append(col)

		self.spots_hit = copy.deepcopy(self.grid)

		for x in range(self.rows):
			for y in range(self.rows):
				self.potential_shots.append((x,y))

	#Returns the Grid
	def get_grid(self):

		return self.grid

	def get_spots_hit(self):

		return self.spots_hit

	def get_potential_shots(self):

		return self.potential_shots

	def set_ship_shots(self,ship_shots):
		self.shop_shots = ship_shots

	def set_hit_ship(self,hit_ship):
		self.hit_ship = hit_ship

	def get_ship_shots(self):
		return self.ship_shots

	def get_hit_ship(self):
		return self.hit_ship

	#Adds the ships to the board
	def add_ships(self):

		#Builds the Ships
		self.ships.append(ship.ship(4,'d','battleship'))
		self.ships.append(ship.ship(4,'e','aircraft carrier'))		
		self.ships.append(ship.ship(3,'b','submarine'))
		self.ships.append(ship.ship(3,'c','cruiser'))
		self.ships.append(ship.ship(2,'a','destroyer'))		

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

		#If the angle is verticle
		ship_len_x = 0
		ship_len_y = ship
		pos_x = 0
		pos_y = 1

		#If the angle is horizontal
		if angle == 1:
			ship_len_x = ship
			ship_len_y = 0
			pos_x = 1
			pos_y = 0

		#Generates a list of potential places
		potential_place = self.select_places(ship_len_x,ship_len_y,potential_place,ship,angle)

		#Checks other angle if no potential position
		if (len(potential_place)<1):
			potential_place = self.select_places(ship_len_y,ship_len_x,potential_place,ship)
		
		#A random position is selected for the ship
		ship_location = randint(0,len(potential_place)-1)
		ship_x = potential_place[ship_location][0]
		ship_y = potential_place[ship_location][1]

		#places the position of the ship on the board
		for x in range(ship):
			self.fill_grid(ship_x,ship_y,pos_x,pos_y,ship,code)

		#Marks the occupied positions on the board
		if angle == 1:

			for x in range(-1,2):
				for y in range(ship_x-1,ship_x+ship+2):
					self.used_spots.append((y,ship_y+x))
		else:

			for x in range(-1,2):
				for y in range(ship_y-1,ship_y+ship+2):
					self.used_spots.append((ship_x+x,y))

		return self.grid

	#Fills the grid with the ships
	def fill_grid(self,x_pos,y_pos,x_inc,y_inc,ship,code):

		for x in range(ship):
			self.grid[x_pos][y_pos] = code

			x_pos += x_inc
			y_pos += y_inc

	#Creates a list of potential places a ship can be placed.
	def select_places(self,left,down,potential_place,ship,angle):

		left = self.grid_size - left
		down = self.grid_size - down

		#Goes across the board and checks the positions the ship will occupy to see if it is valid
		for x in range(left):
			for y in range(down):
				used = False

				for z in range(ship):

					#If the there is a space next to a ship, the position is not valid
					for i in self.used_spots:

						#Different calculations depending on the angle
						if (angle == 0 and (x,y+z) == i): 
							used = True
						elif (angle == 1 and (x+z,y) == i):
							used = True

				#Otherwise the space is a potential space and is added to the list
				if used != True:
					potential_place.append((x,y))

		return potential_place		
