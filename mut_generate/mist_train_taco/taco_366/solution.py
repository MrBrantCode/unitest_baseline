"""
QUESTION:
Given an integer, check whether it is a palindrome or not.
Example 1:
Input: n = 555
Output: Yes
Example 2:
Input: n = 123
Output: No
 
Your Task:
You don't need to read or print anything. Your task is to complete the function is_palindrome() which takes the number as input parameter and returns "Yes" if it is palindrome otherwise returns "No"(Without quotes).
 
Expected Time Complexity: O(x)
Expected Space Complexity: O(x) where x is number of digits in n.
 
Constraints:
1 <= n <= 1000
"""

def is_palindrome(n: int) -> str:
    # Convert the integer to a string
    n_str = str(n)
    
    # Remove any leading/trailing whitespace (though there shouldn't be any)
    n_str = n_str.strip()
    
    # Reverse the string
    reverse_str = n_str[::-1]
    
    # Check if the original string is the same as the reversed string
    if n_str == reverse_str:
        return 'Yes'
    else:
        return 'No'