# Sokoban Puzzle Assignment README

## Overview
This project involves modeling and solving the Sokoban puzzle, a classic game where the player (warehouse keeper) moves boxes onto target spaces within a grid-like warehouse. The objective is to place all boxes on their respective target spaces while adhering to specific movement rules.

## Project Structure
The project is divided into several components:

1. **Modeling the Game State**
   - The game is represented as a two-dimensional grid with various elements:
     - **Player (Robot)**: 'R'
     - **Outside**: 'T'
     - **Wall (Obstacle)**: 'O'
     - **Empty Space**: '   '
     - **Target Space (Storage)**: 'S'
     - **Box (Block)**: 'B'
     - **Player on Target Space**: '.'
     - **Box on Target Space**: '*'
   - The player can move in four directions: UP, DOWN, LEFT, RIGHT.

2. **Node Representation**
   - Each node in the search tree includes:
     - `state`: Current state of the Sokoban puzzle.
     - `parent`: Reference to the parent node.
     - `action`: Action taken to reach the current node.
     - `g`: Path cost (step cost is always 1).
     - `f`: Fitness function for A* algorithm.

3. **Search Algorithms**
   - **Breadth-First Search (BFS)**: A straightforward approach to find a solution.
   - **A* Search**: Utilizes heuristics to find the most efficient solution.

## Heuristic Details
For the A* search algorithm, two heuristics were initially proposed:

1. **Heuristic 1 (h1)**: 
   - Counts the number of boxes that have not yet been placed on target spaces.
   - Formula: 
     \[
     h1(n) = n_{b\_left\_blocks}(n)
     \]

2. **Heuristic 2 (h2)**: 
   - Combines h1 with the estimated number of pushes required to move each box to the nearest target.
   - The Manhattan distance is calculated for each box to its nearest target.
   - Formula:
     \[
     h2(n) = 2 \cdot n_{b\_left\_blocks}(n) + \sum_{b \in B} \min_{s \in S} Manhattan\_distance_{b,s}(n)
     \]

3. **Heuristic 3 (h3)**: 
   - combination of **Heuristic 2 (h2)** and the distance between the player and boxes that are not in the goal state. This approach aims to enhance the efficiency of the A* search by considering both the number of boxes left and their proximity to the player.
   - Formula:
   \[
      h3(n) = h2(n) +  \min_{b \in B} Manhattan\_distance_{b, R}(n)
   \]

## Deadlock Detection
The project also addresses deadlocks, which are states from which no solution can be found. Two types of deadlocks are identified:

1. **Corner Deadlock**: A box is stuck in a corner surrounded by walls.
2. **Line Deadlock**: A box is positioned against a wall with no escape route.

Functions are implemented to detect these deadlocks and improve the A* search algorithm by avoiding subtrees that cannot lead to a solution.

## Game Interface
A graphical user interface (GUI) is created using Pygame to visualize the solution process, displaying the cost and number of steps taken by the different search algorithms.

## Conclusion
This project provides a comprehensive approach to modeling and solving the Sokoban puzzle, utilizing search algorithms and heuristics to enhance performance while addressing potential deadlocks in the game.

## Future Work
Further enhancements could include additional heuristics, optimization of the search algorithms, and more complex puzzle configurations to challenge the solver.

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

The game includes several test examples. You can choose a level by selecting it through the GUI.

### Choosing an Algorithm

When running the solver, you can select which search algorithm to use (BFS or A\*) and specify the heuristic when using A\*.

## GUI Interface

The Pygame GUI displays the Sokoban puzzle grid and animates the steps taken to solve the puzzle. It visualizes the following elements:

- **Player (Robot)**: Represented by  assets/player.png.
- **Wall (Obstacle)**: Represented by assets/obstacle.png.
- **Empty Space**: Represented by assets/ground.png.
- **Target Space (Storage)**: Represented by assets/goal.png.
- **Box (Block)**: Represented by `'B'` assets/box.png.
- **Player on a Target Space**: Represented by a combined player and target image.
- **Box on a Target Space**: Represented by assets/box_target.png.
- **Outside the board**: Represented by assets/outside.png.

After the search algorithm finds a solution, the GUI will simulate the player's moves step by step, showing how the puzzle is solved.


## License

This project is developed for educational purposes as part of the Master 1, Visual Computing program at USTHB.
