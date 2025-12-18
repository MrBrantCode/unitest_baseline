"""
QUESTION:
Given N bits to an AND - Gate find the output that will be produced. 
AND - Gate Table:
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
 
Example 1:
Input:
N = 4
arr: 1 1 1 0
Output:
0
Explanation:
1 & 1 = 1
1 & 1 = 1
1 & 0 = 0
hence output is 0
Example 2:
Input:
N = 4
arr: 0 0 1 0
Output:
0
Explanation:
0 & 0 = 0
0 & 1 = 0
0 & 0 = 0
hence output is 0
Your Task:
You don't need to read input or print anything. Your task is to complete the function andGate() which takes the array arr[], its size N as input parameters and returns the output after processing AND operations on N bits.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=1000
"""

def and_gate(arr, N):
    """
    Computes the output of an AND gate given N bits.

    Parameters:
    arr (list of int): A list of integers (0 or 1) representing the bits.
    N (int): The size of the list arr.

    Returns:
    int: The output of the AND operation on the bits in arr.
    """
    if 0 in arr:
        return 0
    return 1