with open("input.txt", 'r') as fp:
    commands = fp.readline().split(',')

boxes = {i: dict() for i in range(256)}
for k, com in enumerate(commands):
    box = 0
    op_index = com.find('=')
    focal_length = -1
    if op_index > 0:
        label = com[:op_index]
        focal_lenght = int(com[op_index + 1:])
    else:
        label = com[:-1]
    for character in label:
        box += ord(character)
        box = box*17
        box = box % 256
    if op_index > 0:
        boxes[box][label] = focal_lenght
    else:
        if label in boxes[box]:
            boxes[box].pop(label)

focusing_power = 0
for k in boxes.keys():
    for i, k2 in enumerate(boxes[k].keys()):
        focusing_power += (k + 1)*(i + 1) * boxes[k][k2]

print(focusing_power)