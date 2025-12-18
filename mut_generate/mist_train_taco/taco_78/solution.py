"""
QUESTION:
King Tle4Ever of Time Limit Exceeded is really fascinated about Tic Tac Toe. He organizes a national level contest for Tic Tac Toe every year in Time Limit Exceeded. (Though I agree you need to be really stupid to loose a game of Tic Tac Toe but for the sake of question assume playing Tic Tac Toe for them is same as playing Chess for us :P ). 
Every year the contest has lots of participants. This year there are n participants from all over the country. Seeing this huge participation he asks Moron a simple question.
Suppose participant pi wins wi matches. The king wants to know the sum of wi^2 from 1 to n. Now as you already know Moron is not good with maths, he asks you to help him.
Given the value of n find the minimum and maximum value of sum of wi^2 from 1 to n. As values can be too large output the values mod 10^9+7.
[Input]
First line contains a single integer t denoting number of test cases.
Next t lines contains a single integer n denoting the number of participants.

[Output]
For each test case output the minimum and maximum value mod 10^9+7. Say minimum is minx and maximum is maxx than you should print "minx maxx".
[Constraints]
1 ≤ t ≤ 10^5
3 ≤ n ≤ 10^9
NOTE : n will be an odd integer

SAMPLE INPUT
2
3
5

SAMPLE OUTPUT
3 5
20 30
"""

def calculate_min_max_sum_of_squares(t, n_list):
    """
    Calculate the minimum and maximum values of the sum of squares of wins for each test case.

    Parameters:
    t (int): Number of test cases.
    n_list (list of int): List of integers where each integer represents the number of participants for a test case.

    Returns:
    list of tuple: List of tuples where each tuple contains the minimum and maximum values of the sum of squares of wins for a test case.
    """
    mod = 1000000007
    results = []
    
    for n in n_list:
        n1 = n - 1
        matches = n1 * (n1 + 1) // 2
        min_value = int(((matches / n) ** 2 * n) % mod)
        max_value = int((n1 * (n1 + 1) * (2 * n1 + 1) // 6) % mod)
        results.append((min_value, max_value))
    
    return results