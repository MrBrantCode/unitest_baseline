"""
QUESTION:
Selection of Participants of an Experiment

Dr. Tsukuba has devised a new method of programming training. In order to evaluate the effectiveness of this method, he plans to carry out a control experiment. Having two students as the participants of the experiment, one of them will be trained under the conventional method and the other under his new method. Comparing the final scores of these two, he will be able to judge the effectiveness of his method.

It is important to select two students having the closest possible scores, for making the comparison fair. He has a list of the scores of all students who can participate in the experiment. You are asked to write a program which selects two of them having the smallest difference in their scores.

Input

The input consists of multiple datasets, each in the following format.

n
a1 a2 … an

A dataset consists of two lines. The number of students n is given in the first line. n is an integer satisfying 2 ≤ n ≤ 1000. The second line gives scores of n students. ai (1 ≤ i ≤ n) is the score of the i-th student, which is a non-negative integer not greater than 1,000,000.

The end of the input is indicated by a line containing a zero. The sum of n's of all the datasets does not exceed 50,000.

Output

For each dataset, select two students with the smallest difference in their scores, and output in a line (the absolute value of) the difference.

Sample Input


5
10 10 10 10 10
5
1 5 8 9 11
7
11 34 83 47 59 29 70
0


Output for the Sample Input


0
1
5






Example

Input

5
10 10 10 10 10
5
1 5 8 9 11
7
11 34 83 47 59 29 70
0


Output

0
1
5
"""

def find_smallest_score_difference(scores):
    """
    Finds the smallest difference in scores between any two students from a list of scores.

    Parameters:
    scores (list of int): A list of student scores.

    Returns:
    int: The smallest difference in scores.
    """
    if len(scores) < 2:
        raise ValueError("The list must contain at least two scores.")
    
    scores.sort()
    smallest_difference = abs(scores[1] - scores[0])
    
    for i in range(2, len(scores)):
        current_difference = abs(scores[i] - scores[i - 1])
        if current_difference < smallest_difference:
            smallest_difference = current_difference
    
    return smallest_difference