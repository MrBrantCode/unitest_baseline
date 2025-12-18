"""
QUESTION:
Given a number N, swap the two nibbles in it and find the resulting number. 
 
Example 1:
Input:
N = 100
Output:
70
Explanation:
100 in binary is 01100100, 
two nibbles are (0110) and (0100)
If we swap the two nibbles, we get
01000110 which is 70 in decimal
Example 2:
Input:
N = 129
Output:
24
Explanation:
129 in binary is 10000001, 
two nibbles are (1000) and (0001)
If we swap the two nibbles, we get
00011000 which is 24 in decimal
Your Task:
You don't need to read input or print anything. Your task is to complete the function swapNibbles() which takes an integer N as input parameters and returns an integer after swapping nibbles in the binary representation of N.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
0 ≤ N ≤ 255
"""

def swap_nibbles(N: int) -> int:
    """
    Swaps the two nibbles in the binary representation of the given number N.

    Parameters:
    N (int): The input number whose nibbles need to be swapped.

    Returns:
    int: The number after swapping the nibbles.
    """
    # Convert the number to an 8-bit binary string
    binary_str = format(N, '08b')
    
    # Swap the nibbles
    swapped_binary_str = binary_str[4:8] + binary_str[0:4]
    
    # Convert the swapped binary string back to an integer
    result = int(swapped_binary_str, 2)
    
    return result