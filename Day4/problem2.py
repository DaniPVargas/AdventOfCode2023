with open("input.txt", 'r') as fp:
    lines = fp.readlines()

card_numbers = [1 for _ in range(len(lines))]

for i, line in enumerate(lines):
    info = line.split(':')[1].split('|')
    winning_numbers = set(info[0].split())
    my_numbers = set(info[1].split())
    coincidences = len(winning_numbers.intersection(my_numbers))
    for j in range(1, coincidences + 1):
        card_numbers[i + j] += card_numbers[i]

print(sum(card_numbers))