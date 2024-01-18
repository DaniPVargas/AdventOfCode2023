with open("input.txt", 'r') as fp:
    lines = fp.readlines()

points = []
for line in lines:
    info = line.split(':')[1].split('|')
    winning_numbers = set(info[0].split())
    my_numbers = set(info[1].split())
    coincidences = winning_numbers.intersection(my_numbers)
    if len(coincidences) != 0:
        points.append(2**(len(coincidences) - 1))
    else:
        points.append(0)

print(sum(points))