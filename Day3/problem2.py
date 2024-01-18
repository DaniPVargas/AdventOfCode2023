def read_input_file(lines):
    numbers_list = []
    stars_list = []
    for i, l in enumerate(lines):
        j = 0
        while j <= len(l):
            if j == len(l):
                break
            else:
                c = l[j]
                if c == '.':
                    j += 1
                elif c.isdigit():
                    start = j
                    while c.isdigit():
                        j += 1
                        c = l[j]
                    number = int(l[start:j])
                    numbers_list.append((number, i, start, j - 1))
                else:
                    if c == '*':
                        stars_list.append((i,j))
                    j += 1

    return numbers_list, stars_list

def is_adjacent(coordinates, symbol):
    number_line = coordinates[0]
    number_start = coordinates[1]
    number_end = coordinates[2]
    if abs(symbol[0] - number_line) == 1:
        if symbol[1] >= (number_start - 1) and symbol[1] <= (number_end + 1):
            return True
    elif symbol[0] == number_line:
        if symbol[1] == number_start - 1 or symbol[1] == number_end + 1:
            return True 
    return False

def get_gear_ratio(star_coordinates, numbers_list):
    gear_numbers = []
    count = 0
    for number_info in numbers_list:
        number = number_info[0]
        coordinates = number_info[1:]
        if is_adjacent(coordinates, star_coordinates):
            count += 1
            gear_numbers.append(number)
    
    if count == 2:
        prod = gear_numbers[0] * gear_numbers[1]
        return True, prod
    else:
        return False, 0
        

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

sum = 0

numbers_list, stars_list = read_input_file(lines)

for star in stars_list:
    is_gear, gear_ratio = get_gear_ratio(star, numbers_list)
    if is_gear:
        sum += gear_ratio

print(sum)