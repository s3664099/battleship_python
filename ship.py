
#Object that holds the details of the ships
class ship:

	length = 0
	letter = ""
	name = ""
	sunk = False
	hit_sections = []
	co_ordinates = []

	#Sets up the ship
	def __init__(self, length,letter, name):

		self.length = length
		self.letter = letter
		self.name = name
		self.co_ordinates = []
		self.hit_sections = []

		#Fills the sections of the ship with 0, indicating it has not been hit
		for x in self.hit_sections:
			self.hit_sections.append(0)

	#Returns the length of the ship
	def get_length(self):

		return self.length

	#Returns the letter representing the ship
	def get_letter(self):

		return self.letter

	#Returns the name of the ship
	def get_name(self):

		return self.name

	#Gets the flag to see if it is sunk
	def get_sunk(self):

		return self.sunk

	#Adds the co-ordinates of the ship to a list
	def add_coordinate(self,co_ords,inc_x,inc_y,length):

		for x in range(length):
			self.co_ordinates.append(co_ords)
			co_ords = (co_ords[0]+inc_x,co_ords[1]+inc_y)

	#Adds the sections of the ship that has been hit
	def add_hit_sections(self,co_ords):

		self.hit_sections.append(co_ords)

	#Returns the sections that have been hit
	def get_hit_sections(self):
		return self.hit_sections

	#Checks to see if the co-ordinates match the co-ordinates the ship is on.
	def check_coordinates(self,co_ords):

		sunk = False
		found = False

		#Checks if the co-ordinates match
		for x in self.co_ordinates:
			if co_ords == x:
				found = True

		#If there is a match, it is noted, and the co-ordinates are removed
		if found:
			self.co_ordinates.remove(co_ords)
			print("Hit the {}".format(self.name))
			print(len(self.co_ordinates))

		#If there are no co-ordinates left, the ship is marked as sunk
		if len(self.co_ordinates) == 0:
			sunk = True

		return sunk

	#Sinks the ship
	def sink_ship(self):

		self.sunk = True

		return "You sunk my {}".format(self.name)

