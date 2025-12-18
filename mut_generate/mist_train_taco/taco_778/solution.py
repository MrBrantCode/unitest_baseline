"""
QUESTION:
Takahashi is participating in a programming contest, AXC001. He has just submitted his code to Problem A.

The problem has N test cases, all of which must be passed to get an AC verdict.

Takahashi's submission has passed M cases out of the N test cases.

Determine whether Takahashi's submission gets an AC.

-----Constraints-----
 - 1 \leq N \leq 100
 - 0 \leq M \leq N
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N M

-----Output-----
If Takahashi's submission gets an AC, print Yes; otherwise, print No.

-----Sample Input-----
3 3

-----Sample Output-----
Yes

All three test cases have been passed, so his submission gets an AC.
"""

def is_submission_accepted(N: int, M: int) -> str:
    """
    Determines whether Takahashi's submission gets an AC verdict based on the number of test cases passed.

    Parameters:
    - N (int): Total number of test cases.
    - M (int): Number of test cases passed.

    Returns:
    - str: "Yes" if all test cases are passed (N == M), otherwise "No".
    """
    return "Yes" if N == M else "No"