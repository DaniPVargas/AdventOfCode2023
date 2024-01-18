def differences_are_zero(differences):
    for dif in differences:
        if dif != 0:
            return False
    return True

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

entries = [[int(x) for x in l.split()] for l in lines]

entry_values = []
for entry in entries:
    first_values = [entry[0]]
    differences = entry
    while not differences_are_zero(differences):
        differences = [y - x for x,y in zip(differences, differences[1:])]
        first_values.append(differences[0])
    entry_sol = 0
    for num in list(reversed(first_values))[1:]:
        entry_sol = num - entry_sol
    entry_values.append(entry_sol)


print(sum(entry_values))