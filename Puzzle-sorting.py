from collections import deque


def find_neighbor(zero: int) -> list:
    r, c = divmod(zero, 4)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dr, dc in directions:
        x, y = r + dr, c + dc
        if 0 <= x < 4 and 0 <= y < 4:
            neighbors.append(x * 4 + y)
    return neighbors


def print_path(path: list) -> None:
    for step, state in enumerate(path):
        print("step" + str(step) + ":")
        for i in range(0, 16, 4):
            print(state[i:i+4])
        print()


def puzzle_sorting(puzzle: list) -> int:
    goal = tuple(list(range(1, 16)) + [0])
    start = tuple(num for row in puzzle for num in row)

    if start == goal:
        print_path([list(start)])
        return 0

    visited = {start}
    queue = deque([(start, [list(start)])])

    while queue:
        current, path = queue.popleft()

        if current == goal:
            print_path(path)
            return len(path) - 1

        zero_index = current.index(0)
        for move in find_neighbor(zero_index):
            new_list = list(current)
            new_list[zero_index], new_list[move] = new_list[move], new_list[zero_index]
            new_state = tuple(new_list)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_list]))

    return -1


puzzle = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 10, 7, 11],
    [13, 14, 15, 12]
]
moves = puzzle_sorting(puzzle)