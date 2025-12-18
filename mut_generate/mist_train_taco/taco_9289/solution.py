"""
QUESTION:
Panda has started learning about subsets. His professor gave him a simple task. Given a list of numbers, Panda has to choose the subset which gives the maximum product. However, the professor asked Panda only to submit the maximum product obtained by taking exactly two numbers from the list.  Please help Panda in finding out the answer to this assignment.  

Input Format:

The first line will contain the integer N, the length of the array.  The next line contains N space separated integers.

Output Format:

For each test case, output Panda's query.  

Constraints:

2 ≤ N ≤ 10^5

Subtask 1: (25 points)
0 ≤ Integers ≤ 10^9

Subtask 2: (75 points)
-10^9 ≤ Integers ≤ 10^9SAMPLE INPUT
2
2 3

SAMPLE OUTPUT
6

Explanation

The only combination possible is {2,3} whose product is 6 .
"""

def find_max_product_of_two(nums):
    """
    Finds the maximum product of exactly two numbers from the given list.

    Parameters:
    nums (list of int): A list of integers.

    Returns:
    int: The maximum product of two numbers from the list.
    """
    if len(nums) < 2:
        raise ValueError("The list must contain at least two numbers.")
    
    sorted_nums = sorted(nums)
    max_product_with_negatives = sorted_nums[0] * sorted_nums[1]
    max_product_with_positives = sorted_nums[-1] * sorted_nums[-2]
    
    return max(max_product_with_negatives, max_product_with_positives)