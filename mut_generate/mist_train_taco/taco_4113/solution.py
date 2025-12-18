"""
QUESTION:
Given a number in the form of a string of length N . You have to multiply the given number by 11.
Example 1:
Input:
number = "8"
Output: 88
Explanation: 8*11 = 88
Ã¢â¬â¹Example 2:
Input: 
number = "12"
Output: 132
Explanation: 12*11 = 132
Your Task:
You don't need to read input or print anything. Your task is to complete the function multiplyby11() which accepts a string as input parameter and returns a string which should be the multiplication of  number by 11.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
1<= N <=10^{6}
"""

def multiply_by_11(number: str) -> str:
    # Convert the input string to an integer
    num_int = int(number)
    
    # Multiply the integer by 11
    result_int = num_int * 11
    
    # Convert the result back to a string
    result_str = str(result_int)
    
    return result_str