"""
QUESTION:
Ron and Hermione are deep in the Forbidden Forest collecting potion ingredients, and they've managed to lose their way. The path out of the forest is blocked, so they must make their way to a portkey that will transport them back to Hogwarts.  

Consider the forest as an $N\times M$ grid. Each cell is either empty (represented by .) or blocked by a tree (represented by $\mbox{X}$). Ron and Hermione can move (together inside a single cell) LEFT, RIGHT, UP, and DOWN through empty cells, but they cannot travel through a tree cell. Their starting cell is marked with the character $\mbox{M}$, and the cell with the portkey is marked with a $*$. The upper-left corner is indexed as $(0,0)$. 

.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.

In example above, Ron and Hermione are located at index $(2,7)$ and the portkey is at $(1,2)$. Each cell is indexed according to Matrix Conventions.    

Hermione decides it's time to find the portkey and leave. They start along the path and each time they have to choose a direction, she waves her wand and it points to the correct direction. Ron is betting that she will have to wave her wand exactly $\boldsymbol{\mbox{k}}$ times. Can you determine if Ron's guesses are correct?

The map from above has been redrawn with the path indicated as a series where $\mbox{M}$ is the starting point (no decision in this case), $1$ indicates a decision point and $0$ is just a step on the path:

.X.X.10000X
.X*0X0XXX0X
.XX0X0XM01.
...100XXXX.

There are three instances marked with $1$ where Hermione must use her wand.

Note: It is guaranteed that there is only one path from the starting location to the portkey.  

Function Description  

Complete the countLuck function in the editor below.  It should return a string, either $\textbf{Impressed}$ if Ron is correct or $\mathsf{0ops!}$ if he is not.  

countLuck has the following parameters:  

matrix: a list of strings, each one represents a row of the matrix  
k: an integer that represents Ron's guess  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.

Each test case is described as follows: 

The first line contains $2$ space-separated integers $n$ and $m$, the number of forest matrix rows and columns. 

Each of the next $n$ lines contains a string of length $m$ describing a row of the forest matrix. 

The last line contains an integer $\boldsymbol{\mbox{k}}$, Ron's guess as to how many times Hermione will wave her wand.

Constraints

$1\leq t\leq10$  
$1\le n,m\le100$  
$0\leq k\leq10000$  
There will be exactly one $\mbox{M}$ and one $*$ in the forest.  
Exactly one path exists between $\mbox{M}$ and $*$.

Output Format

On a new line for each test case, print $\textbf{Impressed}$ if Ron impresses Hermione by guessing correctly.  Otherwise, print $\mathsf{0ops!}$.

Sample Input
3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4

Sample Output
Impressed
Impressed
Oops!

Explanation

For each test case, $\textit{count}$ denotes the number of times Hermione waves her wand.    

Case 0: Hermione waves her wand at $(0,2)$, giving us $count=1$. Because $count=k=1$, we print $\textbf{Impressed}$ on a new line. 

Case 1: Hermione waves her wand at $(2,9)$, $(0,5)$, and $(3,3)$, giving us $count=3$. Because $count=k=3$, we print $\textbf{Impressed}$ on a new line. 

Case 2: Hermione waves her wand at $(2,9)$, $(0,5)$, and $(3,3)$, giving us $count=3$. Because $count=3$ and $k=4$, $count\neq k$ and we print $\mathsf{0ops!}$ on a new line.
"""

def count_luck(matrix, k):
    def find(matrix, char):
        char_row = [row for row in range(len(matrix)) if char in matrix[row]][0]
        char_col = matrix[char_row].index(char)
        return (char_row, char_col)

    def sum_coords(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def find_path(matrix):
        (N, M) = (len(matrix), len(matrix[0]))
        start = find(matrix, 'M')
        end = find(matrix, '*')
        paths = [[start]]

        def get(coord):
            return matrix[coord[0]][coord[1]]
        
        while paths:
            new_paths = []
            for path in paths:
                for delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    coord = sum_coords(path[-1], delta)
                    if 0 <= coord[0] < N and 0 <= coord[1] < M and (len(path) == 1 or coord != path[-2]) and (get(coord) != 'X'):
                        if coord == end:
                            return path + [coord]
                        else:
                            new_paths.append(path + [coord])
            paths = new_paths
        return None

    def count_waves(matrix, path):
        (N, M) = (len(matrix), len(matrix[0]))

        def get(coord):
            return matrix[coord[0]][coord[1]]
        
        count = 0
        for (i, path_coord) in enumerate(path[:-1]):
            neighbors = [sum_coords(path_coord, delta) for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            options = [coord for coord in neighbors if 0 <= coord[0] < N and 0 <= coord[1] < M and (get(coord) != 'X')]
            if len(options) > (2 if i > 0 else 1):
                count += 1
        return count

    path = find_path(matrix)
    count = count_waves(matrix, path)
    return 'Impressed' if k == count else 'Oops!'