"""
QUESTION:
Given an integer N, find it's parity. 
Parity of a number refers to the number of 1 bits it contains. The number has “odd parity”, if it contains odd number of 1-bits and is “even parity” if it contains even number of 1-bits.
Example 1:
Input:
N = 13
Output: odd
Explanation:
(13)_{10} = (1101)_{2}  The binary representation
has three 1-bits. So, it's parity is odd.
Example 2:
Input:
N = 9
Output: even
Explanation:
(9)_{10} = (1001)_{2}  The binary representation
has two 1-bits. So, it's parity is even.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function computeParity() which takes an Integer N as input parameter and returns string "odd" or "even".
 
Expected Time Complexity: O(log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

def compute_parity(N: int) -> str:
    """
    Computes the parity of the given integer N.

    Parity refers to the number of 1 bits in the binary representation of N.
    If the number of 1 bits is odd, the parity is "odd".
    If the number of 1 bits is even, the parity is "even".

    Parameters:
    N (int): The integer for which to compute the parity.

    Returns:
    str: A string indicating the parity, either "odd" or "even".
    """
    # Convert the integer to its binary representation and count the number of 1 bits
    count_of_ones = bin(N).count('1')
    
    # Determine the parity based on the count of 1 bits
    if count_of_ones % 2 == 0:
        return 'even'
    else:
        return 'odd'