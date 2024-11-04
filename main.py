import pygame
import time
import sys
from game.sokobanPuzzle import SokobanPuzzle
from game.visualizer import Visualizer
from algorithms.bfs import Bfs
from algorithms.astar import AStar

LEVELS = [f"Level {i}" for i in range(1, 8)]
ALGORITHMS = ["BFS", "A*"]
HEURISTICS = ["Heuristic h1", "Heuristic h2", "Heuristic h3"]
DEADLOCK_OPTIONS = ["Without Deadlock Detection", "With Deadlock Detection"]

def displayMenu(screen, title, options, selectedIndex):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    titleText = font.render(title, True, (0, 255, 0))
    screen.blit(titleText, (100, 50))
    
    for idx, option in enumerate(options):
        color = (255, 255, 0) if idx == selectedIndex else (255, 255, 255)
        option_text = font.render(option, True, color)
        screen.blit(option_text, (100, 100 + idx * 40))

    pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Sokoban Menu")

    font = pygame.font.Font(None, 36)

    def display_step(step, goal=False):
        screen.fill((0, 0, 0)) 
        message = f"Step Number: {step}" if not goal else f"Goal! In {step} steps"
        if goal:
            stepText = font.render(message, True, (0, 255, 0))
        else:
            stepText = font.render(message, True, (255, 255, 255))
        screen.blit(stepText, (100, 200))
        pygame.display.flip()
        if goal:
            pygame.time.delay(1000)
      
   
    def menuSelection(title, options):
        selectedIndex = 0
        while True:
            displayMenu(screen, title, options, selectedIndex)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selectedIndex = (selectedIndex + 1) % len(options)
                    elif event.key == pygame.K_UP:
                        selectedIndex = (selectedIndex - 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        return selectedIndex
            pygame.time.delay(100)

    selectedLevel = menuSelection("Select a Level", LEVELS)
    fileName = f"levels/level{selectedLevel + 1}.txt"
    board = SokobanPuzzle(fileName)
    board.load_level()

    selectedAlgorithm = menuSelection("Select an Algorithm", ALGORITHMS)
    if selectedAlgorithm == 0:  
        bfs = Bfs(board)
        path = bfs.bfsSearch(display_step)
    elif selectedAlgorithm == 1: 
        astar = AStar(board)
        selected_heuristic = menuSelection("Select a Heuristic", HEURISTICS)
        if selected_heuristic == 0:
            astar.hFunction = astar.h1
        elif selected_heuristic == 1:
            astar.hFunction = astar.h2
        elif selected_heuristic == 2:
            astar.hFunction = astar.h3

        
        if selectedLevel in [5, 6]:  
            useDeadlock = menuSelection("Use Deadlock Detection?", DEADLOCK_OPTIONS)
            astar.withDeadLock = (useDeadlock == 1) 
        
        path = astar.aStarSearch(display_step)

    visualizer = Visualizer(board)
    for node in path.getPath():
        board = node.state
        visualizer.board = board
        visualizer.update()
        time.sleep(1)

    # Main loop to keep the window open
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
