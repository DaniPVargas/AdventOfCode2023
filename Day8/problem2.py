import re

class NextStepHandler:
    def __init__(self, instructions_list):
        self.instructions = instructions_list
        self.instructions_len = len(instructions_list)
        self.index = 0
    
    def next_step(self):
        step = self.instructions[self.index]
        if self.index == (self.instructions_len - 1):
            self.index = 0
        else:
            self.index += 1

        return step

def get_initial_positions(map_dict):
    positions = []
    for pos in map_dict.keys():
        if pos.endswith('A'):
            positions.append(pos)
    return positions

def check_final_positions(positions):
    for pos in positions:
        if not pos.endswith('Z'):
            return False
    return True

with open("input.txt", 'r') as fp:
    lines = fp.readlines()

instructions = list(lines[0])[:-1]
map_dict = {}
for l in lines[2:]:
    pattern = r"[A-Z]{3}"
    matches = re.findall(pattern, l)
    map_dict[matches[0]] = (matches[1], matches[2])

next_step_handler = NextStepHandler(instructions)
actual_positions = get_initial_positions(map_dict)

for act_pos in actual_positions:
    total_steps = 0
    end_count = 0
    step_count = 0
    while end_count < 2:
        step = next_step_handler.next_step()
        choice = 0 if step == 'L' else 1
        act_pos = map_dict[act_pos][choice]
        total_steps += 1
        step_count += 1
        if act_pos.endswith('Z'):
            print(total_steps)
            end_count += 1
            print(act_pos, step_count)
            step_count = 0
    print('------------------')
exit()

total_steps = 0
while not check_final_positions(actual_positions):
    new_positions = []
    step = next_step_handler.next_step()
    choice = 0 if step == 'L' else 1
    for act_pos in actual_positions:
        new_pos = map_dict[act_pos][choice]
        new_positions.append(new_pos)
    total_steps += 1
    actual_positions = new_positions

print(total_steps)
