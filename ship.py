
#Object that holds the details of the ships
class ship:

	length = 0
	letter = ""
	name = ""
	sunk = False
	hit_sections = []
	co_ordinates = []

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

	def add_coordinate(self,co_ords,inc_x,inc_y,length):

		for x in range(length):
			self.co_ordinates.append(co_ords)
			co_ords = (co_ords[0]+inc_x,co_ords[1]+inc_y)

	def add_hit_sections(self,co_ords):

		self.hit_sections.append(co_ords)

	def get_hit_sections(self):
		return self.hit_sections

	def check_coordinates(self,co_ords):

		sunk = False
		found = False

		for x in self.co_ordinates:
			if co_ords == x:
				found = True

		if found:
			self.co_ordinates.remove(co_ords)
			print("Hit the {}".format(self.name))
			print(len(self.co_ordinates))

		if len(self.co_ordinates) == 0:
			sunk = True

		return sunk

	#Sinks the ship
	def sink_ship(self):

		self.sunk = True

		return "You sunk my {}".format(self.name)

