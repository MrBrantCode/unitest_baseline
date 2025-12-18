"""
QUESTION:
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:

Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101



Example 2:

Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.



Example 3:

Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.



Example 4:

Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""

def has_alternating_bits(n: int) -> bool:
    # Convert the number to its binary representation as a string
    binary_representation = bin(n)[2:]
    
    # Check if each bit alternates with the next one
    for i in range(len(binary_representation) - 1):
        if binary_representation[i] == binary_representation[i + 1]:
            return False
    
    return True