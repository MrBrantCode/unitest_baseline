"""
QUESTION:
Given a number N, print all the numbers which are a bitwise subset of the binary representation of N. Bitwise subset of a number N will be the numbers i in the range 0 ≤ i ≤ N which satisfy the below condition:
N & i == i
Example 1:
Input:
N = 5
Output: 5 4 1 0
Explanation:
   0 & 5 = 0
   1 & 5 = 1
   2 & 5 = 0
   3 & 5 = 1
   4 & 5 = 4
   5 & 5 = 5
  
Example 2:
Input:
N = 9
Output: 9 8 1 0
Your Task:  
You don't need to read input or print anything. Your task is to complete the function printSubsets() which takes the integer N as input parameters and returns the array of integers that satisfy the above condition.
Expected Time Complexity:  O(K), where K is the number of bitwise subsets of N.
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10000
"""

def find_bitwise_subsets(N: int) -> list[int]:
    """
    Finds all numbers i in the range 0 ≤ i ≤ N which satisfy the condition N & i == i.

    Parameters:
    N (int): The integer for which bitwise subsets are to be found.

    Returns:
    list[int]: A list of integers that are bitwise subsets of N, sorted in descending order.
    """
    subsets = []
    for i in range(N + 1):
        if N & i == i:
            subsets.append(i)
    return list(reversed(subsets))