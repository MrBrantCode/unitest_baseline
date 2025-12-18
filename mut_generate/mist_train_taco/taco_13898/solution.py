"""
QUESTION:
Given two numbers N1 and N2, the task is to swap the first digit of the first number with the last digit of the second number and last digit of the first number with the first digit of the second number.
Example 1:
Input:  N1 = "1234", N2 = "5678" 
Output: 8235 4671
Explanation: swap {1, 8} and {4, 5}
Example 2:
Input: N1 = "555", N2 = "55"
Output: 555 55
Explanation: swap {5, 5} and {5, 5}
User Task:
Your task is to complete the function swapDigits() which takes two strings as input and modifies given strings. You do not need to take any input or print anything.
Note: In java code, a custom class Str is used instead of String data type because String in java is passed by value.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
2 <= |N1|, |N2| <= 10^{5}
"""

def swap_digits(n1: str, n2: str) -> tuple:
    # Convert strings to lists to allow modification
    n1_list = list(n1)
    n2_list = list(n2)
    
    # Swap the first digit of n1 with the last digit of n2
    n1_list[0], n2_list[-1] = n2_list[-1], n1_list[0]
    
    # Swap the last digit of n1 with the first digit of n2
    n1_list[-1], n2_list[0] = n2_list[0], n1_list[-1]
    
    # Convert lists back to strings
    modified_n1 = ''.join(n1_list)
    modified_n2 = ''.join(n2_list)
    
    # Return the modified strings as a tuple
    return modified_n1, modified_n2