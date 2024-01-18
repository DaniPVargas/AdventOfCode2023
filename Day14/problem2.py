import numpy as np
from tqdm import tqdm

def slide_rocks(columns):
    new_columns = []
    for col in columns:
        new_col = []
        rock_count = 0
        point_count = 0
        for i in range(len(col)):
            if col[i] == '.':
                point_count += 1
            if col[i] == 'O':
                rock_count += 1
            if col[i] == '#':
                new_col += ['O'] * rock_count + ['.'] * point_count
                new_col += ['#']
                rock_count = 0
                point_count = 0
        if rock_count > 0:
            new_col += ['O'] * rock_count + ['.'] * point_count
        else:
            new_col += ['.'] * point_count
        new_columns.append(new_col)
    
    return new_columns

def make_cycle(rocks_map):
    rocks_map = slide_rocks(rocks_map)
    for _ in range(3):
        rot_map = np.rot90(rocks_map, k=-1)
        rocks_map = slide_rocks(rot_map)
    rocks_map = np.rot90(rocks_map, k=-1)
    return rocks_map


with open("input.txt", 'r') as fp:
    lines = fp.readlines()

rocks_map = [list(x.replace('\n', '')) for x in lines]
rocks_map = np.rot90(rocks_map, k = 1)

final_rocks_map = None
list_previous_maps = [rocks_map.tolist()]
veces_patron = 0
patron_repetido = None

# La idea será buscar un patrón, para que, sabiendo cada cuantos pasos se repite 
# el ciclo, supongamos P pasos, y que el ciclo empieza en el ciclo C, el estado en
# 1e9 será el mismo que en: C + (1e9 - C)%P

for i in range(1000):
    rocks_map = make_cycle(rocks_map).tolist()
    if patron_repetido is not None and rocks_map == patron_repetido:
        tam_ciclo = i - inicio_patron
        break
    if patron_repetido is None and rocks_map in list_previous_maps:
        veces_patron += 1
        inicio_patron = i
        patron_repetido = rocks_map
    list_previous_maps.append(rocks_map)

indice_final = inicio_patron + int((1e9 - inicio_patron))%tam_ciclo
final_rocks_map = np.transpose(np.rot90(list_previous_maps[indice_final], k = -1)).tolist()

rock_weights = 0
for c in final_rocks_map:
    rock_weights += sum([len(c) - i for i, x in enumerate(c) if x == "O"])

print(rock_weights)