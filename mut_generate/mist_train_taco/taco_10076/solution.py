"""
QUESTION:
Given N bits to an OR - Gate find the output that will be produced. 
OR - Gate Table:
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
 
Example 1:
Input:
N = 4
arr: 1 1 1 0
Output:
1
Explanation:
1 | 1 = 1
1 | 1 = 1
1 | 0 = 1
hence output is 1
Example 2:
Input:
N = 4
arr: 0 0 1 0
Output:
1
Explanation:
0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
hence output is 1
Your Task:
You don't need to read input or print anything. Your task is to complete the function orGate() which takes the array arr[], its size N as input parameters and returns the output after processing OR operations on N bits.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=1000
"""

def or_gate(arr, N):
    """
    Computes the output of an OR gate given N bits.

    Parameters:
    arr (list of int): A list of integers (0s and 1s) representing the bits.
    N (int): The size of the list arr.

    Returns:
    int: The output of the OR operation on the bits in arr.
    """
    if 1 in arr:
        return 1
    return 0