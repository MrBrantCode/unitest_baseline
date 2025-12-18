"""
QUESTION:
Given a decimal number N and the base B to which it should be converted. Convert the given number to the given base.
Example 1:
Input:
B = 2
N = 12 
Output:
1100
Explanation:
If the number 12 is converted to a 
number with base 2 we get the binary 
representation of 12 = 1100.
Example 2:
Input:
B = 16
N = 282
Output:
11A
Explanation:
If the number 282 is converted to a 
number with base 16 we get the hexadecimal 
representation of 282 = 11A.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getNumber() which takes two integer B and N representing the base and the decimal number and returns the number in the given base.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
2 <= B <= 16
1 <= N <= 999999999
"""

def convert_decimal_to_base(N: int, B: int) -> str:
    """
    Converts a decimal number N to a number with base B.

    Parameters:
    - N (int): The decimal number to be converted.
    - B (int): The base to which the number should be converted.

    Returns:
    - str: The number N converted to the base B.
    """
    sum = ''
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    while N > 0:
        rem = N % B
        if rem > 9:
            rem_str = hex_dict[rem]
        else:
            rem_str = str(rem)
        sum = rem_str + sum
        N = N // B
    
    return sum