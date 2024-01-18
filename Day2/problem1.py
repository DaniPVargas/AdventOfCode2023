import re

def is_valid_game(rounds, max_blue = 14, max_green = 13, max_red = 12):
    pattern_blue  = r"[0-9]+ blue"
    pattern_red = r"[0-9]+ red"
    pattern_green = r"[0-9]+ green"
    for r in rounds:
        num_blues = 0
        num_reds = 0
        num_green = 0
        blue_cubes = re.findall(pattern_blue, r)
        red_cubes = re.findall(pattern_red, r)
        green_cubes = re.findall(pattern_green, r)
        if len(blue_cubes) != 0:
            num_blues = int(blue_cubes[0].split()[0])
        if len(red_cubes) != 0:
            num_reds = int(red_cubes[0].split()[0])
        if len(green_cubes) != 0:
            num_green = int(green_cubes[0].split()[0])
        if num_blues > max_blue or num_green > max_green or num_reds > max_red:
            return False
    return True

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

ids_sum = 0

for i, game in enumerate(lines):
    rounds = game.split(":")[1].split(";")
    if is_valid_game(rounds):
        ids_sum += i + 1

print(ids_sum)


