"""
QUESTION:
Snuke prepared 6 problems for a upcoming programming contest. For each of those problems, Rng judged whether it can be used in the contest or not.

You are given a string S of length 6. If the i-th character of s is `1`, it means that the i-th problem prepared by Snuke is accepted to be used; `0` means that the problem is not accepted.

How many problems prepared by Snuke are accepted to be used in the contest?

Constraints

* The length of S is 6.
* S consists of `0` and `1`.

Inputs

Input is given from Standard Input in the following format:


S


Outputs

Print the number of problems prepared by Snuke that are accepted to be used in the contest.

Examples

Input

111100


Output

4


Input

001001


Output

2


Input

000000


Output

0
"""

def count_accepted_problems(S: str) -> int:
    """
    Counts the number of problems that are accepted to be used in the contest.

    Parameters:
    S (str): A string of length 6 consisting of '0's and '1's.

    Returns:
    int: The number of '1's in the string S, representing the accepted problems.
    """
    return sum([int(x) for x in S])