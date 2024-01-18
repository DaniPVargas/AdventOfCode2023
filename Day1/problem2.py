import re

with open("./input.txt", 'r') as fp:
    lines = fp.readlines()

pattern = r"[0-9]|oneight|eightwo|twone|one|two|three|four|five|six|seven|eight|nine"
line_numbers = []

for i, l in enumerate(lines):
    temp_list = []
    matches = re.findall(pattern, l)
    for m in matches:
        if m == "oneight":
            temp_list.append(1)
            temp_list.append(8)
        elif m == "eightwo":
            temp_list.append(8)
            temp_list.append(2)
        elif m == "twone":
            temp_list.append(2)
            temp_list.append(1)
        elif m == "one":
            temp_list.append(1)
        elif m == "two":
            temp_list.append(2)
        elif m == "three":
            temp_list.append(3)
        elif m == "four":
            temp_list.append(4)
        elif m == "five":
            temp_list.append(5)
        elif m == "six":
            temp_list.append(6)
        elif m == "seven":
            temp_list.append(7)
        elif m == "eight":
            temp_list.append(8)
        elif m == "nine":
            temp_list.append(9)
        else:
            temp_list.append(int(m))
            
    line_numbers.append(temp_list[0]*10 + temp_list[-1])

print(sum(line_numbers))