"""
QUESTION:
Given an N bit binary number, find the 1's complement of the number. The ones' complement of a binary number is defined as the value obtained by inverting all the bits in the binary representation of the number (swapping 0s for 1s and vice versa).
 
Example 1:
Input:
N = 3
S = 101
Output:
010
Explanation:
We get the output by converting 1's in S
to 0 and 0s to 1
Example 2:
Input:
N = 2
S = 10
Output:
01
Explanation:
We get the output by converting 1's in S
to 0 and 0s to 1
Your Task:  
You don't need to read input or print anything. Your task is to complete the function onesComplement() which takes the binary string S, its size N as input parameters and returns 1's complement of S of size N.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
 
Constraints:
1<=N<=100
"""

def ones_complement(S: str, N: int) -> str:
    """
    Computes the 1's complement of a given N-bit binary number S.

    Parameters:
    S (str): The binary string to compute the 1's complement for.
    N (int): The size of the binary string.

    Returns:
    str: The 1's complement of the binary string S.
    """
    # Initialize the result string
    res = ''
    
    # Iterate through each character in the binary string S
    for bit in S:
        if bit == '0':
            res += '1'
        else:
            res += '0'
    
    # Ensure the result string has the same length as N
    if len(res) != N:
        res = res.ljust(N, '0')
    
    return res