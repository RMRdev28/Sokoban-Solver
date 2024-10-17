# Sokoban Puzzle Solver

## Introduction

This project is a Sokoban puzzle solver implemented in Python using Pygame. The solver utilizes two search algorithms—Breadth-First Search (BFS) and A* Search with various heuristics—to find solutions to Sokoban puzzles. Additionally, a graphical user interface (GUI) is provided to visualize the solutions and the steps taken by the search algorithms.

## Features

- **Sokoban Puzzle Modeling**: Represents the Sokoban game with walls, empty spaces, boxes, target spaces, and the player.
- **Search Algorithms**:
  - **Breadth-First Search (BFS)**: Implements BFS to find a solution to the puzzle.
  - **A\* Search**: Implements A\* Search with multiple heuristics to improve search efficiency.
- **Heuristics**:
  - **Heuristic 1 (h1)**: Counts the number of boxes not yet placed on target spaces.
  - **Heuristic 2 (h2)**: Combines the number of unplaced boxes with the Manhattan distance of each box to the nearest target.
  - **Custom Heuristic (h3)**: An additional heuristic proposed to further optimize A\* Search performance.
- **Graphical User Interface (GUI)**: Uses Pygame to display the puzzle state and animate the steps taken to reach the solution.

## Requirements

- Python 3.x
- Pygame library

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RMRdev28/Sokoban-Solver
   cd sokoban-puzzle-solver
   ```

2. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install pygame
   ```

## Usage

### Running the Solver

To run the Sokoban puzzle solver with the GUI, execute the main Python script:

```bash
python main.py
```

### Selecting a Level

The game includes several test examples as shown in Figure 4 of the assignment. You can choose a level by modifying the `main.py` script or by selecting it through the GUI if implemented.

### Choosing an Algorithm

When running the solver, you can select which search algorithm to use (BFS or A\*) and specify the heuristic when using A\*.

- **To use BFS**:
  ```bash
  python main.py --algorithm bfs
  ```

- **To use A\* with Heuristic 1**:
  ```bash
  python main.py --algorithm astar --heuristic h1
  ```

- **To use A\* with Heuristic 2**:
  ```bash
  python main.py --algorithm astar --heuristic h2
  ```

- **To use A\* with Custom Heuristic**:
  ```bash
  python main.py --algorithm astar --heuristic h3
  ```

### Command-Line Arguments

- `--algorithm`: Specify the search algorithm (`bfs` or `astar`).
- `--heuristic`: Specify the heuristic to use with A\* (`h1`, `h2`, or `h3`).
- `--level`: Specify the level number to solve.

### Example

```bash
python main.py --algorithm astar --heuristic h2 --level 1
```

## GUI Interface

The Pygame GUI displays the Sokoban puzzle grid and animates the steps taken to solve the puzzle. It visualizes the following elements:

- **Player (Robot)**: Represented by `'R'` or an image/icon.
- **Wall (Obstacle)**: Represented by `'O'` or a wall image.
- **Empty Space**: Represented by a blank space or background.
- **Target Space (Storage)**: Represented by `'S'` or a target icon.
- **Box (Block)**: Represented by `'B'` or a box image.
- **Player on a Target Space**: Represented by `'.'` or a combined player and target image.
- **Box on a Target Space**: Represented by `'*'` or a combined box and target image.

After the search algorithm finds a solution, the GUI will simulate the player's moves step by step, showing how the puzzle is solved.

## Implementation Details

### SokobanPuzzle Class

The `SokobanPuzzle` class models the state of the game and includes the following methods:

- `__init__()`: Initializes the state with the grid, player position, box positions, and target positions.
- `isGoal()`: Checks if all boxes are on target spaces.
- `successorFunction()`: Generates all valid moves from the current state, returning pairs of `(action, successor_state)`.

### Node Class

The `Node` class represents nodes in the search tree and includes:

- `state`: The current game state (`SokobanPuzzle` instance).
- `parent`: Reference to the parent node.
- `action`: The action taken to reach this node from the parent.
- `g`: Path cost from the initial state to this node (number of steps).
- `f`: Total estimated cost (`g + h`), used in A\* Search.
- `getPath()`: Returns a list of states representing the path from the initial state to this node.
- `getSolution()`: Returns a list of actions taken to reach this node from the initial state.
- `setF()`: Calculates the fitness function `f` based on the heuristic value `h`.

### Search Algorithms

- **Breadth-First Search (BFS)**: Explores all nodes at the present depth before moving to nodes at the next depth level.
- **A\* Search**: Uses a priority queue ordered by the total estimated cost `f = g + h`, where `h` is the heuristic function.

### Heuristics

- **Heuristic 1 (h1)**:

  ```
  h1(n) = number of boxes not on target spaces
  ```

- **Heuristic 2 (h2)**:

  ```
  h2(n) = 2 * number of boxes not on target spaces + sum over each box of the minimum Manhattan distance to any target
  ```

  For each box `b`, calculate:

  ```
  Manhattan_distance(b, s) = |x_b - x_s| + |y_b - y_s|
  ```

  Then, for each box, take the minimum distance to any target.

- **Custom Heuristic (h3)**:

  A third heuristic proposed to improve the performance of the A\* algorithm. Details should be provided in the documentation or code comments.

### Levels

Test examples (levels) are provided as per Figure 4 in the assignment. Each level's grid configuration is defined in a separate file or within the code. You can add more levels by creating new grid configurations.

## License

This project is developed for educational purposes as part of the Master 1, Visual Computing program at USTHB.

---

**Note**: Make sure to replace `https://github.com/RMRdev28/Sokoban-Solver` with the actual URL of your repository. Update any additional details specific to your implementation, such as file names, additional command-line arguments, or instructions.
