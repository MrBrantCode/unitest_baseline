"""
QUESTION:
This contest, AtCoder Beginner Contest, is abbreviated as ABC.
When we refer to a specific round of ABC, a three-digit number is appended after ABC. For example, ABC680 is the 680th round of ABC.
What is the abbreviation for the N-th round of ABC? Write a program to output the answer.

-----Constraints-----
 - 100 ≤ N ≤ 999

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the abbreviation for the N-th round of ABC.

-----Sample Input-----
100

-----Sample Output-----
ABC100

The 100th round of ABC is ABC100.
"""

def get_abc_round_abbreviation(N: int) -> str:
    """
    Returns the abbreviation for the N-th round of AtCoder Beginner Contest (ABC).

    Parameters:
    N (int): The round number of the contest.

    Returns:
    str: The abbreviation for the N-th round of ABC.
    """
    return 'ABC' + str(N)