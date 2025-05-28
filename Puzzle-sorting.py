from collections import deque


def puzzle_sorting(puzzle):
    purpose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    visited = set()
    start = []

    for x in puzzle:
        for y in puzzle:
            start.append(y)
    puzzle_queue = deque(start)
    visited.add(start)
    step = 0



