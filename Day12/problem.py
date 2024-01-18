from itertools import combinations
import copy
import re
from tqdm import tqdm

def check_distribution(spring_arrangement, conditions):
    pattern = r"1+"
    line = "".join(spring_arrangement)
    springs = [len(m) for m in re.findall(pattern, line)]
    return True if springs == conditions else False

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

ways_count = 0

for k, line in enumerate(lines):
    line_ways_count = 0
    springs_list = line.split()[0]
    conditions = [int (x) for x in line.split()[1].split(",")]
    total_springs = sum(conditions)

    unknown_indexes = [i for i,x in enumerate(springs_list) if x == '?']
    known_springs = springs_list.count("#")

    if total_springs - known_springs == 0:
        line_ways_count += 1
    else:
        springs_combinations = combinations(unknown_indexes, total_springs - known_springs)
        bit_map = ['1' if x == '#' else '0' for x in springs_list]

        for comb in springs_combinations:
            bit_map_copy = bit_map[:]
            for index in comb:
                bit_map_copy[index] = '1'
                if check_distribution(bit_map_copy, conditions):
                    line_ways_count += 1

    ways_count += line_ways_count

print(ways_count)