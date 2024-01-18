# Now, for each empty row or column, we should add one million rows or columns.
# That's impossible for memory reasons, so we are going to try another aproach,
# which could also resolve the first part.

# Setting an universe expansion parameter, in the first iteration we localize each
# galaxy and, knowing how many rows without galaxy are before it, we adjust dinamically
# the correspondant row, but not the column.

# We localize the columns without galaxy in the same way as before, and for each galaxy,
# we count how many columns without galaxy are before the galaxy column, and update 
# that coordinate also. Finally, we compute the distances as before.

# Using universe_expansion = 2, we obtain the results of part one.

import copy
from itertools import combinations

def taxi_distance(coord_1, coord_2):
    return abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1]) 

with open("input.txt", 'r') as fp:
    galaxy_map = [list(x)[:-1] for x in fp.readlines()]

universe_expansion = 1000000
rows_without_galaxy = 0
cols_without_galaxy = []
galaxies_list = []

for i in range(len(galaxy_map)):
    for j in range(len(galaxy_map[i])):
        map_point = galaxy_map[i][j]
        if map_point == '#':
            galaxies_list.append((i + rows_without_galaxy * (universe_expansion - 1), j))
    if galaxy_map[i].count('#') == 0:
        rows_without_galaxy += 1

for col in range(len(galaxy_map[0])):
    col_with_galaxy = False
    for row in range(len(galaxy_map)):
        map_point = galaxy_map[row][col]
        if map_point == '#':
            col_with_galaxy = True
    if not col_with_galaxy:
        cols_without_galaxy.append(col)

final_galaxies_list = []
for position in galaxies_list:
    galaxy_column = position[1]
    minor_col_count = sum([1 for col in cols_without_galaxy if col < galaxy_column])
    galaxy_column = galaxy_column + minor_col_count * (universe_expansion - 1)
    final_galaxies_list.append((position[0], galaxy_column))

combinations_list = list(combinations(final_galaxies_list, 2))
distance_sum = 0

for comb in combinations_list:
    distance_sum += taxi_distance(comb[0], comb[1])

print(distance_sum)