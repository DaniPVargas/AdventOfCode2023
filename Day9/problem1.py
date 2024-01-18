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
    last_values = [entry[-1]]
    differences = entry
    while not differences_are_zero(differences):
        differences = [y - x for x,y in zip(differences, differences[1:])]
        last_values.append(differences[-1])
    entry_values.append(sum(last_values))

print(sum(entry_values))