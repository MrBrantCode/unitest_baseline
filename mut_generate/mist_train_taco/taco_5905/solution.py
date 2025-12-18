"""
QUESTION:
Takahashi is competing in a sumo tournament. The tournament lasts for 15 days, during which he performs in one match per day. If he wins 8 or more matches, he can also participate in the next tournament.

The matches for the first k days have finished. You are given the results of Takahashi's matches as a string S consisting of `o` and `x`. If the i-th character in S is `o`, it means that Takahashi won the match on the i-th day; if that character is `x`, it means that Takahashi lost the match on the i-th day.

Print `YES` if there is a possibility that Takahashi can participate in the next tournament, and print `NO` if there is no such possibility.

Constraints

* 1 \leq k \leq 15
* S is a string of length k consisting of `o` and `x`.

Input

Input is given from Standard Input in the following format:


S


Output

Print `YES` if there is a possibility that Takahashi can participate in the next tournament, and print `NO` otherwise.

Examples

Input

oxoxoxoxoxoxox


Output

YES


Input

xxxxxxxx


Output

NO
"""

def can_participate_in_next_tournament(S: str) -> str:
    """
    Determines if Takahashi can participate in the next tournament based on his match results.

    Parameters:
    S (str): A string of length k consisting of 'o' (win) and 'x' (loss).

    Returns:
    str: 'YES' if there is a possibility that Takahashi can participate in the next tournament, 'NO' otherwise.
    """
    if S.count('x') <= 7:
        return 'YES'
    else:
        return 'NO'