"""
QUESTION:
Petya is having a party soon, and he has decided to invite his $n$ friends.

He wants to make invitations in the form of origami. For each invitation, he needs two red sheets, five green sheets, and eight blue sheets. The store sells an infinite number of notebooks of each color, but each notebook consists of only one color with $k$ sheets. That is, each notebook contains $k$ sheets of either red, green, or blue.

Find the minimum number of notebooks that Petya needs to buy to invite all $n$ of his friends.


-----Input-----

The first line contains two integers $n$ and $k$ ($1\leq n, k\leq 10^8$) — the number of Petya's friends and the number of sheets in each notebook respectively.


-----Output-----

Print one number — the minimum number of notebooks that Petya needs to buy.


-----Examples-----
Input
3 5

Output
10

Input
15 6

Output
38



-----Note-----

In the first example, we need $2$ red notebooks, $3$ green notebooks, and $5$ blue notebooks.

In the second example, we need $5$ red notebooks, $13$ green notebooks, and $20$ blue notebooks.
"""

from math import ceil

def calculate_minimum_notebooks(n: int, k: int) -> int:
    # Calculate the total number of sheets needed for each color
    red_sheets_needed = 2 * n
    green_sheets_needed = 5 * n
    blue_sheets_needed = 8 * n
    
    # Calculate the number of notebooks needed for each color
    red_notebooks_needed = ceil(red_sheets_needed / k)
    green_notebooks_needed = ceil(green_sheets_needed / k)
    blue_notebooks_needed = ceil(blue_sheets_needed / k)
    
    # Sum up the total number of notebooks needed
    total_notebooks_needed = red_notebooks_needed + green_notebooks_needed + blue_notebooks_needed
    
    return total_notebooks_needed