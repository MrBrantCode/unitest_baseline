"""
QUESTION:
The window of Takahashi's room has a width of A. There are two curtains hung over the window, each of which has a horizontal length of B. (Vertically, the curtains are long enough to cover the whole window.)
We will close the window so as to minimize the total horizontal length of the uncovered part of the window.
Find the total horizontal length of the uncovered parts of the window then.

-----Constraints-----
 - 1 \leq A \leq 100
 - 1 \leq B \leq 100
 - A and B are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B

-----Output-----
Print the total horizontal length of the uncovered parts of the window.

-----Sample Input-----
12 4

-----Sample Output-----
4

We have a window with a horizontal length of 12, and two curtains, each of length 4, that cover both ends of the window, for example. The uncovered part has a horizontal length of 4.
"""

def calculate_uncovered_window_length(A: int, B: int) -> int:
    """
    Calculate the total horizontal length of the uncovered parts of the window.

    Parameters:
    - A (int): The width of the window.
    - B (int): The horizontal length of each curtain.

    Returns:
    - int: The total horizontal length of the uncovered parts of the window.
    """
    return max(0, A - 2 * B)