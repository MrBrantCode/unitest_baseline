"""
QUESTION:
Hiking club "Up the hill" just returned from a walk. Now they are trying to remember which hills they've just walked through.

It is known that there were N stops, all on different integer heights between 1 and N kilometers (inclusive) above the sea level. On the first day they've traveled from the first stop to the second stop, on the second day they've traveled from the second to the third and so on, and on the last day they've traveled from the stop N - 1 to the stop N and successfully finished their expedition.

They are trying to find out which heights were their stops located at. They have an entry in a travel journal specifying how many days did they travel up the hill, and how many days did they walk down the hill.

Help them by suggesting some possible stop heights satisfying numbers from the travel journal.


-----Input-----

In the first line there is an integer non-negative number A denoting the number of days of climbing up the hill. Second line contains an integer non-negative number B — the number of days of walking down the hill (A + B + 1 = N, 1 ≤ N ≤ 100 000).


-----Output-----

Output N space-separated distinct integers from 1 to N inclusive, denoting possible heights of the stops in order of visiting.


-----Examples-----
Input
0
1

Output
2 1 

Input
2
1
Output
1 3 4 2
"""

def generate_stop_heights(A: int, B: int) -> list[int]:
    """
    Generates a list of possible stop heights for the hiking club based on the number of days they climbed up and walked down the hill.

    Parameters:
    - A (int): Number of days of climbing up the hill.
    - B (int): Number of days of walking down the hill.

    Returns:
    - list[int]: A list of integers representing the possible heights of the stops in order of visiting.
    """
    N = A + B + 1
    heights = list(range(1, N + 1))
    
    if A == 0:
        return heights[::-1]
    elif B == 0:
        return heights
    else:
        return heights[N - A - 1:] + heights[:N - A - 1][::-1]