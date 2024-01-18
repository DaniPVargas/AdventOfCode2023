def read_input_file(lines):
    numbers_list = []
    symbols_list = []
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
                    if c != '\n':
                        symbols_list.append((i,j))
                    j += 1

    return numbers_list, symbols_list

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

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

sum = 0

numbers_list, symbols_list = read_input_file(lines)

for number in numbers_list:
    coordinates = number[1:]
    for symbol in symbols_list:
        if is_adjacent(coordinates, symbol):
            sum += number[0]
            break

print(sum)