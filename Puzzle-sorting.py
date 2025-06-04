import heapq

def manhattan_distance(state):
    distance = 0
    for idx, val in enumerate(state):
        if val == 0:
            continue
        goal_row, goal_col = divmod(val - 1, 4)
        curr_row, curr_col = divmod(idx, 4)
        distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
    return distance

def find_neighbor(zero: int) -> list:
    r, c = divmod(zero, 4)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        x, y = r + dr, c + dc
        if 0 <= x < 4 and 0 <= y < 4:
            neighbors.append(x * 4 + y)
    return neighbors

def print_path(path: list):
    for step, state in enumerate(path):
        print("step" + str(step) + ":")
        for i in range(0, 16, 4):
            print(state[i:i+4])
        print()

def puzzle_sorting(puzzle):
    start = tuple(num for row in puzzle for num in row)
    goal = tuple(list(range(1, 16)) + [0])

    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            print_path(path)
            return g

        if current in visited:
            continue
        visited.add(current)

        zero_idx = current.index(0)
        for neighbor in find_neighbor(zero_idx):
            new_state = list(current)
            new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
            new_state_tuple = tuple(new_state)
            if new_state_tuple not in visited:
                new_g = g + 1
                new_f = new_g + manhattan_distance(new_state_tuple)
                heapq.heappush(open_set, (new_f, new_g, new_state_tuple, path + [new_state_tuple]))
    return -1

puzzle = [
    [1, 2, 0, 3],
    [5, 6, 7, 4],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]

moves = puzzle_sorting(puzzle)
print("moves :" + str(moves))
