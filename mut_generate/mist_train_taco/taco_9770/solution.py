"""
QUESTION:
A strange grid has been recovered from an old book. It has $5$ columns and infinite number of rows. The bottom row is considered as the first row. First few rows of the grid are like this:

..............

..............

20 22 24 26 28

11 13 15 17 19

10 12 14 16 18

 1  3  5  7  9

 0  2  4  6  8

The grid grows upwards forever!

Your task is to find the integer in $\textbf{C}$^{th} column in $\textbf{r}$^{th} row of the grid.

Input Format

There will be two integers r and c separated by a single space.  

Constraints  

$1\leq r\leq2*10^9$

$1\leq c\leq5$

Rows are indexed from bottom to top and columns are indexed from left to right.  

Output Format

Output the answer in a single line.

Sample Input
6 3

Sample Output
25

Explanation

The number in the 6^{th} row and 3^{rd} column is 25.
"""

def find_grid_value(r: int, c: int) -> int:
    # Adjust row and column to 0-based index
    row = r - 1
    col = c - 1
    
    # Calculate the tens place
    tens = int(row / 2) * 10
    
    # Calculate the ones place
    ones = row % 2 + col * 2
    
    # Calculate the total value
    total = tens + ones
    
    return total