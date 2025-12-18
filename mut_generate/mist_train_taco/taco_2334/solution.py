"""
QUESTION:
Given a non-negative integer N. Check whether the Binary Representation of the number is Palindrome or not. 
Note: No leading 0’s are being considered.
Example 1:
Input:
N = 5
Output: 1
Explanation: The Binary Representation of
5 is 101 which is a Palindrome.
Ã¢â¬â¹Example 2:
Input: 
N = 10
Output: 0
Explanation: The Binary Representation of
10 is 1010 which is not a Palindrome.
Your Task:
You don't need to read input or print anything. Your task is to complete the function binaryPalin() which takes an integer N as input and returns 1 if the binary representation of N is a palindrome. Else, return 0 .
Expected Time Complexity: Log(N). 
Expected Auxiliary Space: O(1).
Constraints:
0<=N<=2^{63}-1
"""

def is_binary_palindrome(N: int) -> int:
    # Convert the integer N to its binary representation, removing the '0b' prefix
    binary_representation = bin(N).replace('0b', '')
    
    # Check if the binary representation is a palindrome
    if binary_representation == binary_representation[::-1]:
        return 1
    else:
        return 0