"""
QUESTION:
A boy Bob likes to draw. Not long ago he bought a rectangular graph (checked) sheet with n rows and m columns. Bob shaded some of the squares on the sheet. Having seen his masterpiece, he decided to share it with his elder brother, who lives in Flatland. Now Bob has to send his picture by post, but because of the world economic crisis and high oil prices, he wants to send his creation, but to spend as little money as possible. For each sent square of paper (no matter whether it is shaded or not) Bob has to pay 3.14 burles. Please, help Bob cut out of his masterpiece a rectangle of the minimum cost, that will contain all the shaded squares. The rectangle's sides should be parallel to the sheet's sides.

Input

The first line of the input data contains numbers n and m (1 ≤ n, m ≤ 50), n — amount of lines, and m — amount of columns on Bob's sheet. The following n lines contain m characters each. Character «.» stands for a non-shaded square on the sheet, and «*» — for a shaded square. It is guaranteed that Bob has shaded at least one square.

Output

Output the required rectangle of the minimum cost. Study the output data in the sample tests to understand the output format better.

Examples

Input

6 7
.......
..***..
..*....
..***..
..*....
..***..


Output

***
*..
***
*..
***


Input

3 3
***
*.*
***


Output

***
*.*
***
"""

def find_minimum_cost_rectangle(n, m, data):
    boundary = [-1, -1, -1, -1]  # [min_col, max_col, min_row, max_row]
    
    # Find the boundary of the shaded area
    for i in range(n):
        for j in range(m):
            if data[i][j] == '*':
                if boundary[0] > j or boundary[0] == -1:
                    boundary[0] = j
                if boundary[1] < j or boundary[1] == -1:
                    boundary[1] = j
                if boundary[2] > i or boundary[2] == -1:
                    boundary[2] = i
                if boundary[3] < i or boundary[3] == -1:
                    boundary[3] = i
    
    # Extract the minimum cost rectangle
    min_cost_rectangle = []
    for i in range(boundary[2], boundary[3] + 1):
        min_cost_rectangle.append(''.join(data[i][boundary[0]:boundary[1] + 1]))
    
    return min_cost_rectangle