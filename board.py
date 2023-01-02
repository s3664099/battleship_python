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
	hit_ship = 0
	hit = (0,0)
	original_hit = (0,0)
	movement = 0

	def __init__(self,object_name):

		#Clears the variables
		self.object_name = object_name
		self.grid = []
		self.used_spots = []
		self.ships = []
		self.grid_size = 9
		self.potential_shots = []
		self.ship_shots = []
		self.hit_ship = 0
		self.hit = (0,0)
		self.movement = 0
		self.original_hit = (0,0)

		#Builds the grid
		for i in range(self.rows):
			col = []
			for j in range(self.rows):
				col.append(".")
			self.grid.append(col)

		#Copys the grid so that the ships are hidden
		self.spots_hit = copy.deepcopy(self.grid)

		#Generates a list of places shots can be made (Currently every space on the board)
		for x in range(self.rows):
			for y in range(self.rows):
				self.potential_shots.append((x,y))

		#Builds the Ships
		self.ships.append(ship.ship(4,'d','battleship'))
		self.ships.append(ship.ship(4,'e','aircraft carrier'))		
		self.ships.append(ship.ship(3,'b','submarine'))
		self.ships.append(ship.ship(3,'c','cruiser'))
		self.ships.append(ship.ship(2,'a','destroyer'))	

	#Returns the Grid
	def get_grid(self):

		return self.grid

	#Returns the Grid without the ships
	def get_spots_hit(self):

		return self.spots_hit

	#Returns the co-ordinates where shots can be made
	def get_potential_shots(self):

		return self.potential_shots

	def set_ship_shots(self,ship_shots):
		self.ship_shots = ship_shots

	def get_ship_shots(self):
		return self.ship_shots

	#Sets and retrieves the variable as to whether a ship has been hit
	def set_hit_ship(self,hit_ship):
		self.hit_ship = hit_ship

	def get_hit_ship(self):
		return self.hit_ship

	def set_hit(self,hit):
		self.hit = hit

	def get_hit(self):
		return self.hit

	#Sets the movement the computer will go in if a ship has been hit more than once
	def set_movement(self,movement):
		self.movement = movement

	def get_movement(self):
		return self.movement

	#Sets the co-ordinate of the original spot the ship was hit
	def set_original_hit(self,hit):
		self.original_hit = hit

	def get_original_hit(self):
		return self.original_hit

	#Get returns the ships
	def get_ships(self):
		return self.ships

	#Adds the ships to the board
	def add_ships(self):

		code = 0

		#Goes through each of the ships and adds them to the board
		for x in self.ships:
			print("{} {} {}".format(x.get_name(),x.get_length(),x.get_letter()))
			self.grid = self.add_ship(x)
			code += 1

	#Adds the ship
	def add_ship(self,ship):

		length = ship.get_length()
		code = ship.get_letter()

		#Creates a list to hold the potential positions the ships can take
		potential_place = []

		#Selects an angle for the ship
		angle = randint(0,1)

		#If the angle is verticle
		ship_len_x = 0
		ship_len_y = length
		pos_x = 0
		pos_y = 1

		#If the angle is horizontal
		if angle == 1:
			ship_len_x = length
			ship_len_y = 0
			pos_x = 1
			pos_y = 0

		#Generates a list of potential places
		potential_place = self.select_places(ship_len_x,ship_len_y,potential_place,length,angle)

		#Checks other angle if no potential position
		if (len(potential_place)<1):
			potential_place = self.select_places(ship_len_y,ship_len_x,potential_place,length,angle)
		
		#A random position is selected for the ship
		ship_location = randint(0,len(potential_place)-1)
		ship_x = potential_place[ship_location][0]
		ship_y = potential_place[ship_location][1]

		return self.place_ship(ship,ship_x,ship_y,pos_x,pos_y,length,code,angle)

	#Places the ship on the board
	def place_ship(self,ship,ship_x,ship_y,pos_x,pos_y,length,code,angle):

		#places the position of the ship on the board
		for x in range(length):
			self.fill_grid(ship_x,ship_y,pos_x,pos_y,length,code)

		ship.add_coordinate((ship_x,ship_y),pos_x,pos_y,length)

		#Marks the occupied positions on the board
		if angle == 1:

			for x in range(-1,2):
				for y in range(ship_x-1,ship_x+length+1):
					self.used_spots.append((y,ship_y+x))
					ship.add_hit_sections((y,ship_y+x))

		else:

			for x in range(-1,2):
				for y in range(ship_y-1,ship_y+length+1):
					self.used_spots.append((ship_x+x,y))
					ship.add_hit_sections((ship_x+x,y))

		return self.grid

	#Checks which ship has been destroyed
	def check_which_ship(self,co_ords,attackers_shots):

		#Sets the ship and win flag
		ship_to_remove = None
		won = 0

		#Goes through each of the ships to check if the ship and co-ordinates match
		for x in self.ships:

			if x.check_coordinates(co_ords):
				ship_to_remove = x
				print(x.sink_ship())
				won = 1

		#Has a ship been found
		if ship_to_remove != None:

			#Marks off all the co-ordinates on the board that was occupied by the ship
			#and removes the ship
			sections_to_mark = ship_to_remove.get_hit_sections()
			self.mark_grid(sections_to_mark,attackers_shots)
			self.ships.remove(ship_to_remove)

		#If no ships are left, the win flag is set.
		if len(self.ships) == 0:
			won = 2

		return won

	#Marks sea sections on both grids as hit since all the ship sections have been hit
	def mark_grid(self,sections_to_mark,attackers_shots):

		for x in sections_to_mark:
			if attackers_shots.count(x)>0:
				self.grid[x[0]][x[1]] = "0"
				self.spots_hit[x[0]][x[1]] = "0"
				attackers_shots.remove(x)

	#Finds the ship, and the sections that need to be hit to destroy the ship
	def get_hit_sections(self,co_ords):

		sections_to_remove = []

		for x in self.ships:
			if x.get_hit_sections().count(co_ords)>1:
				sections_to_remove = x.get_hit_sections
				print(x.get_name())

		return sections_to_remove

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
