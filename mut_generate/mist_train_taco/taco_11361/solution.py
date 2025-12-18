"""
QUESTION:
Mike and some bears are playing a game just for fun. Mike is the judge. All bears except Mike are standing in an n × m grid, there's exactly one bear in each cell. We denote the bear standing in column number j of row number i by (i, j). Mike's hands are on his ears (since he's the judge) and each bear standing in the grid has hands either on his mouth or his eyes. [Image] 

They play for q rounds. In each round, Mike chooses a bear (i, j) and tells him to change his state i. e. if his hands are on his mouth, then he'll put his hands on his eyes or he'll put his hands on his mouth otherwise. After that, Mike wants to know the score of the bears.

Score of the bears is the maximum over all rows of number of consecutive bears with hands on their eyes in that row.

Since bears are lazy, Mike asked you for help. For each round, tell him the score of these bears after changing the state of a bear selected in that round. 


-----Input-----

The first line of input contains three integers n, m and q (1 ≤ n, m ≤ 500 and 1 ≤ q ≤ 5000).

The next n lines contain the grid description. There are m integers separated by spaces in each line. Each of these numbers is either 0 (for mouth) or 1 (for eyes).

The next q lines contain the information about the rounds. Each of them contains two integers i and j (1 ≤ i ≤ n and 1 ≤ j ≤ m), the row number and the column number of the bear changing his state.


-----Output-----

After each round, print the current score of the bears.


-----Examples-----
Input
5 4 5
0 1 1 0
1 0 0 1
0 1 1 0
1 0 0 1
0 0 0 0
1 1
1 4
1 1
4 2
4 3

Output
3
4
3
3
4
"""

def calculate_bear_scores(n, m, q, grid, changes):
    # Convert grid elements to strings for easier manipulation
    grid = [[str(cell) for cell in row] for row in grid]
    
    # Initialize the max_line list with the maximum consecutive '1's for each row
    max_line = [max(map(len, ''.join(row).split('0'))) for row in grid]
    
    # List to store the scores after each round
    scores = []
    
    for (r, c) in changes:
        # Adjust for 0-based indexing
        r -= 1
        c -= 1
        
        # Toggle the state of the bear
        grid[r][c] = '0' if grid[r][c] == '1' else '1'
        
        # Recalculate the maximum consecutive '1's for the changed row
        max_line[r] = max(map(len, ''.join(grid[r]).split('0')))
        
        # Append the current score to the scores list
        scores.append(max(max_line))
    
    return scores