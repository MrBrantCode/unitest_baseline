"""
QUESTION:
Given an integer N, write a program to find the one’s complement of the integer.
 
Example 1:
Input:
N = 5
Output:
2
Explanation:
binary of 5 is 101
1's complement of 101 is 010
010 is 2 in its decimal form. 
Example 2:
Input:
N = 255
Output:
0
Explanation:
binary of 255 is 1111 1111
1's complement of 1111 1111 is
0000 0000 which is 0 in its decimal form.
Your Task:
You don't need to read input or print anything. Your task is to complete the function onesComplement() which takes an integer N as input parameter and returns an integer value, the one's complement of N.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

def ones_complement(N: int) -> int:
    """
    Calculate the one's complement of a given integer N.

    Parameters:
    N (int): The integer for which the one's complement is to be calculated.

    Returns:
    int: The one's complement of the integer N.
    """
    binary_representation = bin(N)[2:]
    complement_binary = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
    return int(complement_binary, 2)