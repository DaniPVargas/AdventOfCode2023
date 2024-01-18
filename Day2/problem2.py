import re

def get_set_power(rounds):
    pattern_blue  = r"[0-9]+ blue"
    pattern_red = r"[0-9]+ red"
    pattern_green = r"[0-9]+ green"
    max_red = 0
    max_blue = 0
    max_green = 0
    for r in rounds:
        blue_cubes = re.findall(pattern_blue, r)
        red_cubes = re.findall(pattern_red, r)
        green_cubes = re.findall(pattern_green, r)
        if len(blue_cubes) != 0:
            num_blues = int(blue_cubes[0].split()[0])
            if num_blues > max_blue:
                max_blue = num_blues
        if len(red_cubes) != 0:
            num_reds = int(red_cubes[0].split()[0])
            if num_reds > max_red:
                max_red = num_reds
        if len(green_cubes) != 0:
            num_green = int(green_cubes[0].split()[0])
            if num_green > max_green:
                max_green = num_green
    
    return max_blue * max_green * max_red
        

power_sum = 0

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

for i, game in enumerate(lines):
    rounds = game.split(":")[1].split(";")
    power_sum += get_set_power(rounds)

print(power_sum)