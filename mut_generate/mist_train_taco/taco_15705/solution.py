"""
QUESTION:
So the Chef has become health conscious and is now lifting weights at the gym. But its his first time so the trainer gives him a simple job to do. 

He has been given a weight lifting rod and N heavy weights, each weighing 20, 21, .... , 2n-1. He has to stick each of the "N" weights on the rod, one after another, in such a way that the right side is never heavier than the left side. At each step he chooses one of the weights that has not yet been fixed on the rod, and fix it on either the left side of the rod or the right, until all of the weights have been placed.

Now help the chef and find out, in how many ways the chef can accomplish this?

-----Input-----
First line of input contains an integer T, the number of test cases. Then T test cases follow. Each line of test case contains one integer, N denoting the number of weights

-----Output-----
The output contains T lines, each containing an integer denoting all possible combinations

-----Example-----
Input:
3
2
5
18

Output:
3
945
221643095476699771875
"""

def calculate_weight_combinations(n: int) -> int:
    """
    Calculate the number of ways to place weights on a rod such that the right side is never heavier than the left side.

    Parameters:
    n (int): The number of weights (2^0, 2^1, ..., 2^(n-1)).

    Returns:
    int: The number of possible combinations.
    """
    if n <= 0:
        return 0
    
    fact = 1
    start = 1
    for i in range(1, n + 1):
        fact *= start
        start += 2
    
    return fact