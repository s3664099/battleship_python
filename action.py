from random import randint

#Determines the move that the attacker is going to make
def fire(defender,attacker):

	#Sets the variables used in the algorithm
	#Including information from the previous turn
	original_hit = (0,0)
	shot = (0,0)
	grid = defender.get_grid()
	spots_hit = defender.get_spots_hit()
	hit_ship = defender.get_hit_ship()
	hit_result = 0
	potential_shots = attacker.get_potential_shots()

	#A ship has been previously hit once
	if hit_ship == 1:

		#Gets the previous hit and sets it as the original
		hit = defender.get_hit()
		original_hit = hit
		ship_shots = defender.get_ship_shots()

		#Selects a random shot from the shots that can be made
		#And removes it from the list
		shot = randint(0,len(ship_shots)-1)
		select_shot = ship_shots[shot]
		ship_shots.remove(select_shot)
		defender.set_movement(select_shot)

		shot = get_next_shot(select_shot,hit)

		#Checks if there are more potential shots, and removes them
		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	#If a ship has been hit more than once
	elif hit_ship == 2:

		#Checks the direction it is heading, and continue in that direction
		ship_shots = defender.get_ship_shots()
		hit = defender.get_hit()
		shot = defender.get_movement()
		shot = get_next_shot(shot,hit)

		#Checks if there are more potential shots, and removes them
		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	else:

		#Otherwise selects a random shot from the list of potential shots
		shot = randint(0,len(potential_shots)-1)
		shot = potential_shots[shot]

		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	result = "0"

	#Has this empty spot already been hit?
	if grid[shot[0]][shot[1]] == "0":
		grid[shot[0]][shot[1]] = "."

	#The spot isn't empty
	if grid[shot[0]][shot[1]] != ".":

		#Marks it as a ship
		result = "X"

		#Sets the flag that a ship has been hit and checks if it has been sunk
		defender.set_hit(shot)
		hit_result = defender.check_which_ship (shot,potential_shots)

		#If a ship wasn't hit previously, sets the flag
		if hit_ship == 0:
			defender.set_hit_ship(1)
			ship_shots = check_ship_shots(potential_shots,shot)
			defender.set_ship_shots(ship_shots)

		#It it has, sets it that it has been hit more than once
		if hit_ship == 1:		
			defender.set_hit_ship(2)
			defender.set_original_hit(original_hit)

			#Sets the next potential shot in case the shot misses
			if select_shot == 0:
				ship_shots = [1]
			elif select_shot == 1:
				ship_shots = [0]
			elif select_shot == 2:
				ship_shots = [3]
			else:
				ship_shots = [2]

			defender.set_ship_shots(ship_shots)

	#If it was a miss
	else:

		#If the previous shots hit the ship, then goes back to the original spot
		#And sets it in the opposite direction
		if hit_ship == 2:
			defender.set_hit_ship(1)
			defender.set_hit(defender.get_original_hit())
		else:
			print("Shot fired at: {}".format(shot))

	#Updates the grids
	grid[shot[0]][shot[1]] = result
	spots_hit[shot[0]][shot[1]] = result

	#Has the ship been sunk
	if hit_result == 1:
		defender.set_hit_ship(0)

	return hit_result

#Gest the next shots from when the ship was hit
def get_next_shot(selected,hit):

	if selected == 0:
		shot = (hit[0]+1,hit[1])
	elif selected == 1:
		shot = (hit[0]-1,hit[1])
	elif selected == 2:
		shot = (hit[0],hit[1]+1)
	else:
		shot = (hit[0],hit[1]-1)

	return shot

#Checks to see if the potential shots once the ship is hit haven't already been taken.
#if they haven't, it adds the potential shot to the list
def check_ship_shots(potential_shots,shot):

	ship_shots = []

	if potential_shots.count((shot[0]+1,shot[1])) >0:
		ship_shots.append(0)
	if potential_shots.count((shot[0]-1,shot[1])) >0:
		ship_shots.append(1)
	if potential_shots.count((shot[0],shot[1]+1)) >0:
		ship_shots.append(2)
	if potential_shots.count((shot[0],shot[1]-1)) >0:
		ship_shots.append(3)

	return ship_shots