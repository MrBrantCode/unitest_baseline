"""
QUESTION:
Given a Binary Number B, find its decimal equivalent.
 
Example 1:
Input: B = 10001000
Output: 136
Example 2:
Input: B = 101100
Output: 44
 
Your Task:
You don't need to read or print anything. Your task is to complete the function binary_to_decimal() which takes the binary number as string input parameter and returns its decimal equivalent.
 
Expected Time Complexity: O(K * Log(K)) where K is number of bits in binary number.
Expected Space Complexity: O(1)
 
Constraints:
1 <= number of bits in binary number  <= 16
"""

def binary_to_decimal(binary_str: str) -> int:
    """
    Converts a binary number represented as a string to its decimal equivalent.

    Parameters:
    binary_str (str): The binary number as a string.

    Returns:
    int: The decimal equivalent of the binary number.
    """
    return int(binary_str, 2)