"""
QUESTION:
Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.
 
Example 1: 
Input:
N = 5
vector = {1, 1, 1, 1, 1}
X = 1
Output: 
5
Explanation: Frequency of 1 is 5.
Your Task:
Your task is to complete the function findFrequency() which should count the frequency of X and return it.
"""

def find_frequency(arr, x):
    """
    Finds the frequency of the integer x in the list arr.

    Parameters:
    arr (list of int): The list of positive integers.
    x (int): The integer whose frequency needs to be found.

    Returns:
    int: The frequency of x in the list arr.
    """
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count