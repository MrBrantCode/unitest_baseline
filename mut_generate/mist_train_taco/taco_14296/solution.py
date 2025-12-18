"""
QUESTION:
Given a number N and its base b, convert it to decimal. The base of number can be anything such that all digits can be represented using 0 to 9 and A to Z. Value of A is 10, value of B is 11 and so on.
Example 1:
Input: b = 2, N = 1100
Output: 12
Explaination: It is a binary number whose 
decimal equivalent is 12.
Example 2:
Input: b = 16, N = A
Output: 10
Explaination: It's a hexadecimal number whose 
decimal equivalent is 10.
Your Task:
You do not need to read input or print anything. Your task is to complete the function decimalEquivalent() which takes N and b as input parameters and returns their decimal equivalent. Otherwise return -1 if N is not possible.
Expected Time Complexity: O(|N|)   [|N| means the length of the number N]
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ b ≤ 16
1 ≤ N < decimal equivalent 10^{9}
"""

def convert_to_decimal(N: str, b: int) -> int:
    """
    Converts a number N in base b to its decimal equivalent.

    Parameters:
    - N (str): The number to be converted (as a string).
    - b (int): The base of the number N.

    Returns:
    - int: The decimal equivalent of the number N in base b.
           Returns -1 if N is not a valid number in base b.
    """
    valid_digits = '0123456789ABCDEF'
    
    # Check if all characters in N are valid for the given base b
    for char in N:
        if char not in valid_digits[:b]:
            return -1
    
    # Convert the number to decimal
    try:
        return int(N, b)
    except ValueError:
        return -1