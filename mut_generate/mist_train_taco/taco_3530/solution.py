"""
QUESTION:
Given two binary strings A and B that represent value of two integers, find the product of two strings in Decimal Value.
 
Example 1:
Input:
A = "1100" , B = "01"
Output:
12
Explanation:
Decimal representation of A is 12 and
that of B is 1. So, A*B gives the
output 12.
Example 2:
Input:
A = "01" , B = "01"
Output:
1
Explanation:
Decimal representation of both A and 
B is 1. So, A*B gives the output 1.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function karatsubaAlgo() which takes Strings A and B as input and returns the answer.
 
Expected Time Complexity: O(Length of Binary String)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |A|,|B| <= 25
"""

def multiply_binary_strings(A: str, B: str) -> int:
    """
    Multiplies two binary strings and returns the product in decimal form.

    Parameters:
    A (str): The first binary string.
    B (str): The second binary string.

    Returns:
    int: The product of the two binary strings in decimal form.
    """
    # Convert binary strings to decimal integers
    a = int(A, 2)
    b = int(B, 2)
    
    # Calculate the product
    product = a * b
    
    return product