import sys
import time
import subprocess
# model related settings
maze_area = []  # model
blocked_square = '#'
free_square = ' '  # whitespace
steps_mark = '*'
start = 'A'
goal = 'B'
maze_area_delimiter = '|'

# search related data
node = []
state = None
frontier = []
explored_nodes = []
is_in_goal = False


# map .txt file to a data structure
def maze_mapper(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            maze_area.append(list(line.rstrip('\n').replace('|', '')))


# check out the action that can be taken
def actions(state):
    possible_movements = ([1, 0], [0, 1], [-1, 0], [0, -1])  # possible movements in cartesian plan for a square

    for movement in possible_movements:
        try:
            action_to_pick = [state[0] + movement[0], state[1] + movement[1]]

            if action_to_pick[0] >= 0 and action_to_pick[1]>=0 and maze_area[action_to_pick[0]][action_to_pick[1]] == free_square or maze_area[action_to_pick[0]][action_to_pick[1]] == goal:
                frontier.append(action_to_pick)

        except:
            1 == 1

    if len(frontier) >= 1:
        selected_node = frontier[len(frontier) - 1]
        explored_nodes.append(frontier[len(frontier) -1])
        frontier.pop(len(frontier) - 1)
        return selected_node

    return None


def output_maze(file_path):
    with open(file_path.replace(".txt", "")+"-result.txt", 'w') as file:
        for node_line in maze_area:
            str_line = ""
            for node in node_line:
                str_line = str_line+node
                file.write(node)
            print(str_line)
            file.write("\n")

def model_transformation(state):
    global is_in_goal
    if maze_area[state[0]][state[1]] == 'B':
        is_in_goal = True
    else:
        maze_area[state[0]][state[1]] = '*'
    return state


def start_state(model, value):
    for i, row in enumerate(model):
        for j, cell in enumerate(row):
            if cell == value:
                return i, j
    return None


# get file path passed when run python3 maze.py [maze environment file here*.txt]
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    file_path = sys.argv[1]
    maze_mapper(file_path)

    state = start_state(maze_area, start)

    while not is_in_goal:
        state = actions(state)

        if state is None:
            print("There is no way!")
            break


        state = model_transformation(state)
        subprocess.call(['clear'])
        output_maze(file_path)
        time.sleep(0.2)

    print("\n")
    print("Explored nodes", explored_nodes)
    print("Spent steps:", len(explored_nodes))