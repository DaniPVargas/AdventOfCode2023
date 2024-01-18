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


with open("input.txt", 'r') as fp:
    lines = fp.readlines()

instructions = list(lines[0])[:-1]
map_dict = {}
for l in lines[2:]:
    pattern = r"[A-Z]{3}"
    matches = re.findall(pattern, l)
    map_dict[matches[0]] = (matches[1], matches[2])

next_step_handler = NextStepHandler(instructions)
actual_position = 'AAA'
total_steps = 0
while actual_position != 'ZZZ':
    step = next_step_handler.next_step()
    choice = 0 if step == 'L' else 1
    actual_position = map_dict[actual_position][choice]
    total_steps += 1

print(total_steps)


