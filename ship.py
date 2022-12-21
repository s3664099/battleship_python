
#Object that holds the details of the ships
class ship:

	length = 0
	letter = ""
	name = ""
	sunk = False
	hit_sections = []

	def __init__(self, length,letter, name):

		self.length = length
		self.letter = letter
		self.name = name

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

	#Flags that the ship has been hit
	def hit_ship(self):

		hit = False
		x = 0

		#Cycles through the hit sections
		while not hit:

			#If a section is undamaged it is marked at hit
			if self.hit_sections[x] == 0:

				self.hit_sections[x] = 1
			
			x += 1

		undamage = False
		destroyed = False
		
		#Cycles through again to see if the ship is still afloat
		while not undamage:

			#If there is an undamaged part, it flags an undamaged section
			if self.hit_sections[x] == 0:
				undamage = True

		#No undamaged section found
		if not undamage:
			destroyed = True

		return destroyed

	#Sinks the ship
	def sink_ship(self):

		self.sunk = True

		return "You sunk my {}".format(self.name)

