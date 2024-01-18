def slide_rocks(columns):
    new_columns = []
    for col in columns:
        new_col = []
        rock_count = 0
        point_count = 0
        for i in range(len(col)):
            if col[i] == '.':
                point_count += 1
            if col[i] == 'O':
                rock_count += 1
            if col[i] == '#':
                new_col += ['O'] * rock_count + ['.'] * point_count
                new_col += ['#']
                rock_count = 0
                point_count = 0
        if rock_count > 0:
            new_col += ['O'] * rock_count + ['.'] * point_count
        else:
            new_col += ['.'] * point_count
        new_columns.append(new_col)
    
    return new_columns

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

columns = list(map(list, zip(*lines)))
new_columns = slide_rocks(columns)

rock_weights = 0
for c in new_columns:
    rock_weights += sum([len(c) - i for i, x in enumerate(c) if x == "O"])

print(rock_weights)



