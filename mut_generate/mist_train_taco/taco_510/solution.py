"""
QUESTION:
You are enthusiastically participating in Virtual Boot Camp-14 and want to seriously learn programming. To be a good programmer you not only need to solve a problem, but also need to solve it as quickly as possible. 

You are participating in this "Week02 Contest" and want to win it. You are sure that you will be able to solve all the questions in this contest, but to become Rank 1, you need to solve every problem in least amount of time with least number of wrong attempts.

The person solving maximum # of problems with least amount of time penalty wins the contest.So before solving any harder problem in the contest, you want to be prepared with a program which calculates time penalty for you. 

You know that you start the contest at exactly 1/7/14 00:00 and end the contest at D/7/14 HH:MM with W #number of wrong attempts. [One wrong attempt adds 20 minutes to your time penalty] 

You have to output the final time penalty.

Note: For simplicity we assume we have only one problem to solve during the contest

INPUT FORMAT:

Line 1: 4 Integers D H M W

CONSTRAINTS:

1 ≤ D ≤ 5

0 ≤ H ≤ 23

0 ≤ M ≤ 59

0 ≤ W ≤ 10^8

OUTPUT FORMAT:

Line 1: Time Penalty in Minutes

SAMPLE INPUT
5 0 0 100000000

SAMPLE OUTPUT
2000005760
"""

def calculate_time_penalty(D: int, H: int, M: int, W: int) -> int:
    """
    Calculate the total time penalty for a contest based on the end time and number of wrong attempts.

    Parameters:
    D (int): The day of the contest end (1 ≤ D ≤ 5).
    H (int): The hour of the contest end (0 ≤ H ≤ 23).
    M (int): The minute of the contest end (0 ≤ M ≤ 59).
    W (int): The number of wrong attempts (0 ≤ W ≤ 10^8).

    Returns:
    int: The total time penalty in minutes.
    """
    # Calculate the total time penalty
    time_penalty = (D - 1) * 24 * 60 + (20 * W) + (H * 60) + M
    return time_penalty