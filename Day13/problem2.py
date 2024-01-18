def check_simmetry(row, pattern):
    index_1 = row
    index_2 = row + 1
    steps = min([index_1 + 1, len(pattern) - index_2])
    wrong_tiles = 0
    for j in range(steps):
        if pattern[index_1 - j] != pattern[index_2 + j]:
            for x, y  in zip(pattern[index_1 - j], pattern[index_2 + j]):
                if x != y:
                    wrong_tiles += 1
    
    if wrong_tiles == 1:
        return True
    else:
        return False

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

# File reading
patterns = []
individual_pat = []
for k, l in enumerate(lines):
    l = l.replace('\n', '')
    if l == '':
        patterns.append(individual_pat)
        individual_pat = []
    else:
        if k == len(lines) - 1:
            individual_pat.append(l)
            patterns.append(individual_pat)
            individual_pat = []
        else:
            individual_pat.append(l)

# Simmetry count
sum = 0
for k, pat in enumerate(patterns):
    simmetry_column_count, simmetry_row_count = 0, 0
    # 1. Check vertical simmetry
    for i in range(len(pat) - 1):
        if check_simmetry(i, pat):
            simmetry_row_count += i + 1
            break

    # 2. If there is not vertical simmetry, check horizontal simmetry
    if simmetry_row_count == 0:
        columns = ["".join([row[i] for row in pat]) for i in range(len(pat[0]))]
        for i in range(len(columns) - 1):
            if check_simmetry(i, columns):
                simmetry_column_count += i + 1
                break

    sum += 100 * simmetry_row_count + simmetry_column_count

print(sum)

