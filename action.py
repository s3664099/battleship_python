from random import randint

def fire(defender,attacker):

	original_hit = (0,0)
	shot = (0,0)
	grid = defender.get_grid()
	spots_hit = defender.get_spots_hit()
	hit_ship = defender.get_hit_ship()
	hit_result = 0
	potential_shots = attacker.get_potential_shots()

	if hit_ship == 1:
		hit = defender.get_hit()
		original_hit = hit
		ship_shots = defender.get_ship_shots()

		shot = randint(0,len(ship_shots)-1)
		select_shot = ship_shots[shot]
		ship_shots.remove(select_shot)
		defender.set_movement(select_shot)

		shot = get_next_shot(select_shot,hit)

		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	elif hit_ship == 2:
		ship_shots = defender.get_ship_shots()
		hit = defender.get_hit()
		shot = defender.get_movement()
		shot = get_next_shot(shot,hit)

		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	else:
		shot = randint(0,len(potential_shots)-1)
		shot = potential_shots[shot]

		if potential_shots.count(shot)>0:
			potential_shots.remove(shot)

	result = "0"

	if grid[shot[0]][shot[1]] == "0":
		grid[shot[0]][shot[1]] = "."

	if grid[shot[0]][shot[1]] != ".":

		result = "X"
		defender.set_hit(shot)
		hit_result = defender.check_which_ship (shot,potential_shots)

		if hit_ship == 0:
			defender.set_hit_ship(1)
			ship_shots = [0,1,2,3]
			defender.set_ship_shots(ship_shots)
		if hit_ship == 1:		
			defender.set_hit_ship(2)
			defender.set_original_hit(original_hit)

			if select_shot == 0:
				ship_shots = [1]
			elif select_shot == 1:
				ship_shots = [0]
			elif select_shot == 2:
				ship_shots = [3]
			else:
				ship_shots = [2]

			defender.set_ship_shots(ship_shots)

	else:
		if hit_ship == 2:
			defender.set_hit_ship(1)
			defender.set_hit(defender.get_original_hit())

	grid[shot[0]][shot[1]] = result
	spots_hit[shot[0]][shot[1]] = result

	if hit_result == 1:
		defender.set_hit_ship(0)

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