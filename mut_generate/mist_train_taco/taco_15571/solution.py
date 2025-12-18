"""
QUESTION:
Welcome to PC Koshien, players. This year marks the 10th anniversary of Computer Koshien, but the number of questions and the total score will vary from year to year. Scores are set for each question according to the difficulty level. When the number of questions is 10 and the score of each question is given, create a program that outputs the total of them.



input

The input is given in the following format.


s1
s2
..
..
s10


The input consists of 10 lines, and the i line is given the integer si (0 ≤ si ≤ 100) representing the score of problem i.

output

Output the total score on one line.

Example

Input

1
2
3
4
5
6
7
8
9
10


Output

55
"""

def calculate_total_score(scores: list) -> int:
    """
    Calculate the total score from a list of scores.

    Parameters:
    scores (list): A list of integers representing the scores of 10 problems.

    Returns:
    int: The total score.
    """
    return sum(scores)