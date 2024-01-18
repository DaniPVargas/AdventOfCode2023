class NextPositionHelper:
    def __init__(self, maze, pos_inicial, next_pos):
        self.maze = maze
        self.pos_anterior = pos_inicial
        self.next_pos = next_pos
        self.pos_list = [pos_inicial, next_pos]
    
    def get_position_list(self):
        return self.pos_list

    def get_next_position(self):
        pipe = self.maze[self.next_pos[0]][self.next_pos[1]]
        if pipe == '7':
            if self.next_pos[0] == self.pos_anterior[0]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] + 1, self.next_pos[1])
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] - 1)
        elif pipe == 'F':            
            if self.next_pos[0] == self.pos_anterior[0]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] + 1, self.next_pos[1])
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] + 1)
        elif pipe == 'J':
            if self.next_pos[0] == self.pos_anterior[0]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] - 1, self.next_pos[1])
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] - 1)
        elif pipe == 'L':
            if self.next_pos[0] == self.pos_anterior[0]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] - 1, self.next_pos[1])
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] + 1)
        elif pipe == '|':
            if self.next_pos[0] < self.pos_anterior[0]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] - 1, self.next_pos[1])
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0] + 1, self.next_pos[1])
        elif pipe == '-':            
            if self.next_pos[1] < self.pos_anterior[1]:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] - 1)
            else:
                self.pos_anterior = self.next_pos
                self.next_pos = (self.next_pos[0], self.next_pos[1] + 1)
        self.pos_list.append(self.next_pos)
        return self.next_pos

def get_initial_pipe(ini_pos, posiciones_iniciales):
    up, down, left, right = False, False, False, False

    for pos in posiciones_actuales:
        if pos[0] == ini_pos[0]:
            if pos[1] < ini_pos[1]:
                left = True
            else:
                right = True
        else:
            if pos[0] < ini_pos[0]:
                up = True
            else:
                down = True
    
    if up:
        if left:
            return "J"
        if right:
            return "L"
        if down: return "|"
    else:
        if down:
            if left:
                return "7"
            if right:
                return "F"
        else:
            return "-"

with open("input.txt", 'r') as fp:
    maze = fp.readlines()

# 1. Localizamos la posición de inicio
for i, l in enumerate(maze):
    if l.count('S') > 0:
        ini_pos = (i, l.index('S'))
        break

posiciones_actuales = []

# 2. Buscamos las dos tuberías conectadas
if ini_pos[0] != 0:
    if maze[ini_pos[0] - 1][ini_pos[1]] in set(['7', 'F', '|']):
        posiciones_actuales.append((ini_pos[0] - 1, ini_pos[1]))
if ini_pos[0] != (len(maze) - 1):
    if maze[ini_pos[0] + 1][ini_pos[1]] in set(['|', 'L', 'J']):
        posiciones_actuales.append((ini_pos[0] + 1, ini_pos[1]))
if ini_pos[1] != 0:
    if maze[ini_pos[0]][ini_pos[1] - 1] in set(['-', 'L', 'F']):
        posiciones_actuales.append((ini_pos[0], ini_pos[1] - 1))
if ini_pos[1] != (len(maze[0]) - 1):
    if maze[ini_pos[0]][ini_pos[1] + 1] in set(['-', '7', 'J']):
        posiciones_actuales.append((ini_pos[0], ini_pos[1] + 1))

if len(posiciones_actuales) != 2:
    print("--------- ERROR AL LEER LAS POSICIONES INICIALES --------")

pos_camino_1 = posiciones_actuales[0]
pos_camino_2 = posiciones_actuales[1]

helper_camino_1 = NextPositionHelper(maze, ini_pos, pos_camino_1)
helper_camino_2 = NextPositionHelper(maze, ini_pos, pos_camino_2)

# 3. Calculamos la siguiente posición en bucle hasta que se encuentren
steps_taken = 1
while pos_camino_1 != pos_camino_2:
    pos_camino_1 = helper_camino_1.get_next_position()
    pos_camino_2 = helper_camino_2.get_next_position()
    steps_taken += 1

print(f"Steps to the furthest point: {steps_taken}")

# 4. Problem Part 2

# 4.1 Get complete path
path_1 = helper_camino_1.get_position_list()
path_2 = helper_camino_2.get_position_list()
complete_path = list(set(path_1).union(set(path_2)))

initial_pipe = get_initial_pipe(ini_pos, posiciones_actuales)
maze[ini_pos[0]] = maze[ini_pos[0]].replace('S', initial_pipe)

tiles_count = 0

# Iterating per line
for i in range(len(maze)):
    j = 0
    zone = 0
    while j < len(maze[i]):
        pipe = maze[i][j]
        if (i,j) in complete_path:
            if pipe == '|':
                zone += 1
            elif pipe == 'L':
                j += 1
                pipe = maze[i][j]
                while pipe == '-':
                    j += 1
                    pipe = maze[i][j]
                if pipe == "J":
                    zone += 2
                else:
                    zone += 1
            
            elif pipe == 'F':
                j += 1
                pipe = maze[i][j]
                while pipe == '-':
                    j += 1
                    pipe = maze[i][j]
                if pipe == "7":
                    zone += 2
                else:
                    zone += 1    
            j += 1
        else:
            if (i,j) not in complete_path and zone % 2 == 1:
                tiles_count += 1
            j += 1
'''
# Iterating for each element not in the pipe
tiles_inside = []
for i in range(len(maze)):
    for j in range(len(maze[i])):
        pipe = maze[i][j]
        if (i,j) not in complete_path:
            count = 0
            k = j + 1
            while k < len(maze[i]):
                char = maze[i][k]
                if (i,k) in complete_path:
                    if char == '|':
                        count += 1
                    if char == 'L':
                        while char not in set(['7', 'J']):
                            k += 1
                            char = maze[i][k]
                        if char == 'J':
                            count += 2
                        else:
                            count += 1
                    if char == 'F':
                        while char not in set(['7', 'J']):
                            k += 1
                            char = maze[i][k]
                        if char == '7':
                            count += 2
                        else:
                            count += 1
                k += 1
            if count % 2 == 1:
                tiles_inside.append((i,j))
                tiles_count += 1
'''

print(tiles_count)