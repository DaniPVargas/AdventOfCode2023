import copy
from itertools import combinations

def taxi_distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1]) 

with open("input.txt", 'r') as fp:
    galaxy_map = [list(x)[:-1] for x in fp.readlines()]

# 1. Detect rows and columns without galaxies:
rows_without_galaxy = []
cols_without_galaxy = []

for i in range(len(galaxy_map)):
    row_with_galaxy = False
    for j in range(len(galaxy_map[i])):
        map_point = galaxy_map[i][j]
        if map_point == '#':
            row_with_galaxy = True
    if not row_with_galaxy:
        rows_without_galaxy.append(i)

for col in range(len(galaxy_map[0])):
    col_with_galaxy = False
    for row in range(len(galaxy_map)):
        map_point = galaxy_map[row][col]
        if map_point == '#':
            col_with_galaxy = True
    if not col_with_galaxy:
        cols_without_galaxy.append(col)

# 2. Apply universe expansion
empty_row = ['.'] * len(galaxy_map[0])
# 2.1 Duplicate rows without galaxies
for i, index in enumerate(rows_without_galaxy):
    galaxy_map.insert(i + index, empty_row)
# 2.2 Duplicate cols without galaxy
for i, row in enumerate(galaxy_map):
    new_row = copy.copy(row)
    for j, index in enumerate(cols_without_galaxy):
        new_row.insert(j + index, '.')
    galaxy_map[i] = new_row

# 3. Obtain new ubications of galaxies
galaxies_list = []

for i in range(len(galaxy_map)):
    for j in range(len(galaxy_map[i])):
        if galaxy_map[i][j] == '#':
            galaxies_list.append((i,j))
        
# 4. Obtain combinations of two galaxies, and compute the distance (taxi distance)
combinations_list = list(combinations(galaxies_list, 2))
distance_sum = 0

for comb in combinations_list:
    distance_sum += taxi_distance(comb[0], comb[1])

print(distance_sum)