from tqdm import tqdm

def leer_mapa():
    c = input()
    mapa = []
    c = input()
    while c:
        t = tuple([int(x) for x in c.split()])
        mapa.append(t)
        c = input()
    
    return mapa

def obtener_posicion_mapa(number, mapping):
    for entry in mapping:
        if entry[1] <= number <= (entry[1] + entry[2] - 1):
            distance = number - entry[1]
            return entry[0] + distance

    return number

def obtener_posicion_final(number, maps):
    for mapping in maps:
        number = obtener_posicion_mapa(number, mapping)
    
    return number

seeds_line = input()
seeds = [int(x) for x in seeds_line.split(":")[1].split()]
input()
maps = []
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())

final_positions = []
for seed in tqdm(seeds):
    final_positions.append(obtener_posicion_final(seed, maps))

print(min(final_positions))