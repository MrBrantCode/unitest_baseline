"""
QUESTION:
Lenny is playing a game on a 3 × 3 grid of lights. In the beginning of the game all lights are switched on. Pressing any of the lights will toggle it and all side-adjacent lights. The goal of the game is to switch all the lights off. We consider the toggling as follows: if the light was switched on then it will be switched off, if it was switched off then it will be switched on.

Lenny has spent some time playing with the grid and by now he has pressed each light a certain number of times. Given the number of times each light is pressed, you have to print the current state of each light.


-----Input-----

The input consists of three rows. Each row contains three integers each between 0 to 100 inclusive. The j-th number in the i-th row is the number of times the j-th light of the i-th row of the grid is pressed.


-----Output-----

Print three lines, each containing three characters. The j-th character of the i-th line is "1" if and only if the corresponding light is switched on, otherwise it's "0".


-----Examples-----
Input
1 0 0
0 0 0
0 0 1

Output
001
010
100

Input
1 0 1
8 8 8
2 0 3

Output
010
011
100
"""

def get_light_grid_state(press_counts):
    # Initialize the grid with all lights on
    grid = [[1 for _ in range(5)] for __ in range(5)]
    
    # Process each light press
    for i in range(3):
        for j in range(3):
            presses = press_counts[i][j]
            if presses % 2 == 1:
                # Toggle the light and its adjacent lights
                grid[i + 1][j + 1] = 1 - grid[i + 1][j + 1]
                grid[i + 2][j + 1] = 1 - grid[i + 2][j + 1]
                grid[i][j + 1] = 1 - grid[i][j + 1]
                grid[i + 1][j + 2] = 1 - grid[i + 1][j + 2]
                grid[i + 1][j] = 1 - grid[i + 1][j]
    
    # Extract the inner 3x3 grid and convert to string representation
    result = [
        [str(grid[i + 1][j + 1]) for j in range(3)]
        for i in range(3)
    ]
    
    return result