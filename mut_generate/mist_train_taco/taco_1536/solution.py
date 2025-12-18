"""
QUESTION:
Given a positive integer N, print count of set bits in it. 
Example 1:
Input:
N = 6
Output:
2
Explanation:
Binary representation is '110' 
So the count of the set bit is 2.
Example 2:
Input:
8
Output:
1
Explanation:
Binary representation is '1000' 
So the count of the set bit is 1.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function setBits() which takes an Integer N and returns the count of number of set bits.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def count_set_bits(N: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of a given positive integer N.

    Parameters:
    N (int): The positive integer for which to count the set bits.

    Returns:
    int: The count of set bits in the binary representation of N.
    """
    count = 0
    while N != 0:
        count += N & 1
        N >>= 1
    return count