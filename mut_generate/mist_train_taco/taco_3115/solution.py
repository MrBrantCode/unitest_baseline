"""
QUESTION:
Young boy Artem tries to paint a picture, and he asks his mother Medina to help him. Medina is very busy, that's why she asked for your help.

Artem wants to paint an $n \times m$ board. Each cell of the board should be colored in white or black. 

Lets $B$ be the number of black cells that have at least one white neighbor adjacent by the side. Let $W$ be the number of white cells that have at least one black neighbor adjacent by the side. A coloring is called good if $B = W + 1$. 

The first coloring shown below has $B=5$ and $W=4$ (all cells have at least one neighbor with the opposite color). However, the second coloring is not good as it has $B=4$, $W=4$ (only the bottom right cell doesn't have a neighbor with the opposite color). [Image] 

Please, help Medina to find any good coloring. It's guaranteed that under given constraints the solution always exists. If there are several solutions, output any of them.


-----Input-----

Each test contains multiple test cases. 

The first line contains the number of test cases $t$ ($1 \le t \le 20$). Each of the next $t$ lines contains two integers $n, m$ ($2 \le n,m \le 100$) — the number of rows and the number of columns in the grid.


-----Output-----

For each test case print $n$ lines, each of length $m$, where $i$-th line is the $i$-th row of your colored matrix (cell labeled with 'B' means that the cell is black, and 'W' means white). Do not use quotes.

It's guaranteed that under given constraints the solution always exists.


-----Example-----
Input
2
3 2
3 3

Output
BW
WB
BB
BWB
BWW
BWB


-----Note-----

In the first testcase, $B=3$, $W=2$.

In the second testcase, $B=5$, $W=4$. You can see the coloring in the statement.
"""

def generate_good_coloring(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m = case
        grid = []
        
        # Generate the alternating pattern for the first n-1 rows
        for i in range(n - 1):
            row = ''
            for j in range(m):
                if (i + j) % 2 == 0:
                    row += 'B'
                else:
                    row += 'W'
            grid.append(row)
        
        # Generate the last row to ensure B = W + 1
        last_row = ''
        for j in range(m):
            if j == 0:
                last_row += 'B'
            elif j % 2 == 0:
                last_row += 'W'
            else:
                last_row += 'B'
        grid.append(last_row)
        
        # Append the grid for this test case to the results
        results.append(grid)
    
    return results