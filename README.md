# Puzzle-Sorting

A small Python project that implements and compares different search/sorting strategies for solving sliding-tile puzzles (e.g. the classic 8-puzzle). It provides a command-line interface to load a puzzle, choose an algorithm and heuristic, and then solves the puzzle while reporting performance metrics.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Algorithms & Heuristics](#algorithms--heuristics)  
- [Code Structure](#code-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

Sliding-tile puzzles consist of a grid of numbered tiles with one empty space. The goal is to reorder the tiles into a target configuration by sliding tiles into the empty space. This repository provides:

- Multiple search strategies to find a solution path  
- Configurable heuristics to guide informed searches  
- Detailed statistics on moves, visited states, and runtime  

---

## Features

- **Uninformed searches**:  
  - Breadth-First Search (BFS)  
  - Depth-First Search (DFS)  
- **Informed searches**:  
  - A* Search  
  - Iterative Deepening A* (IDA*)  
- **Heuristics**:  
  - Manhattan Distance  
  - Misplaced Tiles Count  
  - (Optional) Euclidean Distance  
- **Command-line interface**: specify puzzle, algorithm, heuristic, and verbosity  
- **Performance reporting**:  
  - Number of moves in solution  
  - Total states expanded  
  - Time to solve  

---

## Requirements

- Python 3.7 or later  
- Standard library only (no external dependencies)  

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mahajialirezaei/Puzzle-sorting.git
   cd Puzzle-sorting
  

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Ensure you have Python 3 installed:

   ```bash
   python --version
   ```

---

## Usage

```bash
python Puzzle-sorting.py [OPTIONS] START_STATE [GOAL_STATE]
```

* `START_STATE`: comma-separated list of tile values, row by row, using `0` for the blank.
* `GOAL_STATE` (optional): same format as `START_STATE`. Defaults to `1,2,…,N−1,0`.
* **Options**:

  * `--algorithm`, `-a`: one of `bfs`, `dfs`, `astar`, `ida` (default: `astar`)
  * `--heuristic`, `-h`: one of `manhattan`, `misplaced` (default: `manhattan`)
  * `--max-depth`, `-d`: maximum search depth (for DFS/IDA\*)
  * `--verbose`, `-v`: print intermediate states and stats

### Examples

Solve the classic 8-puzzle (3×3) from a random start:

```bash
python Puzzle-sorting.py -a astar -h misplaced 1,2,3,4,5,6,7,8,0
```

Run a DFS with depth limit 20 on a 15-puzzle:

```bash
python Puzzle-sorting.py -a dfs -d 20 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0
```

---

## Algorithms & Heuristics

### Uninformed Strategies

* **BFS**: guarantees shortest-move solution but can exhaust memory.
* **DFS**: low memory footprint but may wander into deep, unpromising branches.

### Informed Strategies

* **A\***: best-first search guided by `f(n) = g(n) + h(n)`.
* **IDA\***: combines iterative deepening with heuristic pruning.

### Heuristics

1. **Manhattan Distance**
   Sum of vertical + horizontal distances of each tile from its goal position.
2. **Misplaced Tiles**
   Count of tiles not in their goal position.

---

## Code Structure

```
.
├── .idea/                    ← IDE project settings (can be ignored)
└── Puzzle-sorting.py         ← Main solver script
```

* **Puzzle-sorting.py**

  * Parses command-line arguments
  * Defines `PuzzleState` class (state representation, moves)
  * Implements search functions (`bfs()`, `dfs()`, `astar()`, `ida()`)
  * Defines heuristic functions
  * Reports solution path and performance metrics

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add YourFeature"`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

---

## 🛠 Developer

Developed by [Mohammad Amin Haji Alirezaei](https://github.com/mahajialirezaei)
Feel free to ⭐️ this repo or open an issue if you'd like to contribute or have questions!
This project is released under the **MIT License**. See [LICENSE](LICENSE) for details.

```
::contentReference[oaicite:0]{index=0}
```
