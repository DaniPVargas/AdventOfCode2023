with open("input.txt", 'r') as fp:
    lines = fp.readlines()

times = [int(x) for x in lines[0].split(":")[1].split()]
distances = [int(x) for x in lines[1].split(":")[1].split()]
races = [(x,y) for x,y in zip(times, distances)]

options_per_race = []
for race in races:
    max_time = race[0]
    max_distance = race[1]
    options = 0
    for i in range(1, max_time):
        if i*(max_time  - i) > max_distance:
            options += 1
    options_per_race.append(options)

result = 1
for opts in options_per_race:
    result = result * opts

print(result)
