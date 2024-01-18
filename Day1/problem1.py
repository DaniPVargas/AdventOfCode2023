import re

with open("./input.txt", 'r') as fp:
    lines = fp.readlines()

line_numbers = []
pattern = r"[0-9]"

for l in lines:
    matches = re.findall(pattern, l)
    line_numbers.append(int(matches[0])*10 + int(matches[-1]))

print(sum(line_numbers))