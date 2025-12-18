"""
QUESTION:
The city of Fishtopia can be imagined as a grid of 4 rows and an odd number of columns. It has two main villages; the first is located at the top-left cell (1,1), people who stay there love fishing at the Tuna pond at the bottom-right cell (4, n). The second village is located at (4, 1) and its people love the Salmon pond at (1, n).

The mayor of Fishtopia wants to place k hotels in the city, each one occupying one cell. To allow people to enter the city from anywhere, hotels should not be placed on the border cells.

A person can move from one cell to another if those cells are not occupied by hotels and share a side.

Can you help the mayor place the hotels in a way such that there are equal number of shortest paths from each village to its preferred pond?

Input

The first line of input contain two integers, n and k (3 ≤ n ≤ 99, 0 ≤ k ≤ 2×(n-2)), n is odd, the width of the city, and the number of hotels to be placed, respectively.

Output

Print "YES", if it is possible to place all the hotels in a way that satisfies the problem statement, otherwise print "NO".

If it is possible, print an extra 4 lines that describe the city, each line should have n characters, each of which is "#" if that cell has a hotel on it, or "." if not.

Examples

Input

7 2


Output

YES
.......
.#.....
.#.....
.......


Input

5 3


Output

YES
.....
.###.
.....
.....
"""

def can_place_hotels(n, k):
    EMPTY = '.'
    HOTEL = '#'
    
    if k > 2 * (n - 2):
        return False, None
    
    grid = [EMPTY * n for _ in range(4)]
    
    if k % 2 == 0:
        m = k // 2
        s = EMPTY + HOTEL * m + EMPTY * (n - m - 1)
        grid[1] = s
        grid[2] = s
    elif k < n - 1:
        s = (HOTEL * k).center(n, EMPTY)
        grid[1] = s
    else:
        grid[1] = EMPTY + HOTEL * (n - 2) + EMPTY
        grid[2] = EMPTY + HOTEL * (k - n + 1) + EMPTY * (2 * n - k - 4) + HOTEL + EMPTY
    
    return True, grid