import sys
sys.setrecursionlimit(10000)

def is_solvable(state):
    check_ls = [x for x in state if x !=0]
    check_flag = 0
    for i in range(15):
        for j in range(i+1, 15):
            if check_ls[i] > check_ls[j]:
                check_flag += 1
    zero_idx = state.index(0)
    zero_row_from_top = zero_idx // 4
    row_from_bottom = 4 - zero_row_from_top

    return (check_flag + row_from_bottom) % 2 == 1

def manhattan_distance(state):
    distance = 0
    for idx, val in enumerate(state):
        if val == 0:
            continue
        goal_row, goal_col = divmod(val - 1, 4)
        curr_row, curr_col = divmod(idx, 4)
        distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
    return distance

def find_neighbors(zero_idx):
    r, c = divmod(zero_idx, 4)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        x, y = r + dr, c + dc
        if 0 <= x < 4 and 0 <= y < 4:
            neighbors.append(x * 4 + y)
    return neighbors


def print_path(path):
    for step, state in enumerate(path):
        print("step :" + str(step))
        for i in range(0, 16, 4):
            print(state[i:i+4])
        print()

def puzzle_sorting(start, goal):

    path = [start]
    zero_idx = start.index(0)
    threshold = manhattan_distance(start)

    result_path = None

    def dfs(state, g, threshold, zero_idx, prev_zero):
        nonlocal result_path

        h = manhattan_distance(state)
        f = g + h

        if f > threshold:
            return f

        if state == goal:
            result_path = path.copy()
            return "FOUND"

        min_threshold = float('inf')

        neighbors = find_neighbors(zero_idx)
        for neighbor in neighbors:
            if neighbor == prev_zero:
                continue

            new_state = list(state)
            new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
            new_state_tuple = tuple(new_state)

            path.append(new_state_tuple)
            temp = dfs(new_state_tuple, g + 1, threshold, neighbor, zero_idx)
            if temp == "FOUND":
                return "FOUND"
            if isinstance(temp, int) and temp < min_threshold:
                min_threshold = temp
            path.pop()

        return min_threshold

    while True:
        temp = dfs(start, 0, threshold, zero_idx, -1)
        if temp == "FOUND":
            return result_path
        if temp == float('inf'):
            return None
        threshold = temp

puzzle = [
    [1, 2, 0, 3],
    [5, 6, 7, 4],
    [9, 10, 11, 8],
    [13, 14, 15, 12]
]



start_state = tuple(num for row in puzzle for num in row)
goal_state = tuple(list(range(1, 16)) + [0])


if not is_solvable(start_state):
    print("not solvable")

else :
    solution_path = puzzle_sorting(start_state, goal_state)
    if solution_path is not None:
        print("moves :" + str(len(solution_path) - 1))
        print_path(solution_path)
    else:
        print("not found")
