"""
QUESTION:
Given a number N. check whether a given number N  is palindrome or not in it's both formates (Decimal and Binary ).
Example 1:
Input: N = 7
Output: "Yes" 
Explanation: 7 is palindrome in it's decimal 
and also in it's binary (111).So answer is "Yes".
Example 2:
Input: N = 12
Output: "No"
Explanation: 12 is not palindrome in it's decimal
and also in it's binary (1100).So answer is "No". 
Your Task:  
You don't need to read input or print anything. Complete the function isDeciBinPalin() which takes N as input parameter and returns "Yes" if N is a palindrome in its both formates else returns "No".
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{7}
"""

def is_deci_bin_palin(n: int) -> str:
    # Convert the number to its binary representation
    binary_representation = bin(n)[2:]  # bin(n) returns '0b...' so we slice off the '0b'
    
    # Check if the decimal representation is a palindrome
    decimal_str = str(n)
    decimal_is_palindrome = decimal_str == decimal_str[::-1]
    
    # Check if the binary representation is a palindrome
    binary_is_palindrome = binary_representation == binary_representation[::-1]
    
    # Return "Yes" if both are palindromes, otherwise "No"
    if decimal_is_palindrome and binary_is_palindrome:
        return "Yes"
    else:
        return "No"