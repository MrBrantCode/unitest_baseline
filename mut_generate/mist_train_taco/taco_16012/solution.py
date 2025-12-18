"""
QUESTION:
Given 'n', print the symbol 'Z' spanning n rows using '*' symbol.
Value of n>2 and n ≤ 20.

Example:
1) Input : n=3
Output:
***
 *
***

2) Input n=4
Output:
****
  *
 *
****

SAMPLE INPUT
5

SAMPLE OUTPUT
*****
   *
  *
 *
*****

Explanation

The 'Z' is printed across 5 lines as shown above.
"""

def print_z_pattern(n):
    # Initialize an empty list to store the rows of the 'Z' pattern
    z_pattern = []
    
    # First row is all '*'
    z_pattern.append('*' * n)
    
    # Middle rows
    for i in range(1, n-1):
        # Create a string with spaces and a single '*' at the correct position
        middle_row = ' ' * (n - i - 1) + '*'
        z_pattern.append(middle_row)
    
    # Last row is all '*'
    z_pattern.append('*' * n)
    
    return z_pattern