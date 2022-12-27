from random import randint

def fire(grid,spots_hit,potential_shots):

	print(len(potential_shots))
	shot = randint(0,len(potential_shots))
	shot = potential_shots[shot]

	result = "X"

	if grid[shot[0]][shot[1]] == ".":
		result = "0"
	grid[shot[0]][shot[1]] = result
	spots_hit[shot[0]][shot[1]] = result

	potential_shots.remove(shot)
	print(len(potential_shots))
