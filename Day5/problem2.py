from tqdm import tqdm
import math

def leer_mapa():
    c = input()
    mapa = []
    c = input()
    while c:
        t = tuple([int(x) for x in c.split()])
        mapa.append(t)
        c = input()
    mapa = sorted(mapa, key=lambda x: x[1])
    return mapa

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
        else:
            merged_intervals.append(interval)

    return merged_intervals

def aplicar_mapping_intervalo(interval, mapping):
    final_intervals = []
    for rule in mapping:
        if interval == []:
            break
        ini_source = rule[1]
        fin_source = rule[1] + rule[2] - 1
        ini_dest = rule[0]
        fin_dest = ini_dest + rule[2] - 1
        if interval[1] < ini_source:
            final_intervals.append(interval)
            interval = []
        elif interval[0] > fin_source:
            pass
        elif interval[0] >= ini_source and interval[1] <= fin_source:
            distance_ini = interval[0] - ini_source
            distance_fin = interval[1] - ini_source
            result = [ini_dest + distance_ini, ini_dest + distance_fin]
            final_intervals.append(result)
            interval = []
        elif interval[0] < ini_source < interval[1] and fin_source > interval[1]:
            # affected_interval = [ini_source, interval[0]]
            transformed_interval = [ini_dest, ini_dest + interval[1] - ini_source]
            final_intervals.append(transformed_interval)
            final_intervals.append([interval[0], ini_source - 1])
            interval = []
        elif interval[0] < fin_source < interval[1] and ini_source < interval[0]:
            # affected_interval = [interval[0], fin_source]
            transformed_interval = [ini_dest + interval[0] - ini_source, fin_dest]
            final_intervals.append(transformed_interval)
            interval = [fin_source + 1, interval[1]]
        elif interval[0] < ini_source and fin_source < interval[1]:
            # affected_interval = [ini_source, fin_source]
            transformed_interval = [ini_dest, fin_dest]
            final_intervals.append(transformed_interval)
            final_intervals.append([interval[0], ini_source - 1])
            interval = [fin_source + 1, interval[1]]

    if interval != []:
        final_intervals.append(interval)
    return final_intervals

def aplicar_mappings(intervalo, maps):
    intervals = [intervalo]
    for mapping in maps:
        stage_intervals = []
        for interval in intervals:
            stage_intervals += aplicar_mapping_intervalo(interval, mapping)
        intervals = merge_intervals(stage_intervals)
    return intervals

seeds_line = input()
seeds = [int(x) for x in seeds_line.split(":")[1].split()]
intervalos = []
for i in range(0, len(seeds), 2):
    pair = seeds[i:i+2]
    intervalos.append([pair[0], pair[0] + pair[1] - 1])
input()
maps = []
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())
maps.append(leer_mapa())

intervalos_finales = []
for interval in intervalos:
    intervalos_finales += aplicar_mappings(interval, maps)

resultado_final = merge_intervals(intervalos_finales)
print(resultado_final[0][0])
