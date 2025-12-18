"""
QUESTION:
Ricky gives a number 'n' to John. Now Ricky wants John to generate Z with symbol "*" such that it spans n rows.

Example:

Input : n=3

Output :

***
  *
***

Input : n=4

Output :

****
   *
  *
****

Constraint :

3 ≤ n ≤20

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

def generate_z_pattern(n: int) -> list[str]:
    # Initialize an empty list to store the rows of the pattern
    pattern = []
    
    # First row: all '*'
    pattern.append('*' * n)
    
    # Middle rows: spaces followed by a single '*'
    for i in range(n-2):
        pattern.append(' ' * (n-i-2) + '*')
    
    # Last row: all '*'
    pattern.append('*' * n)
    
    return pattern