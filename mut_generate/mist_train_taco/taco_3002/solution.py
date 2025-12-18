"""
QUESTION:
Given a number S in the form of string, the task is to find if it's divisible by 36 or not. 
 
Example 1:
Input:
S = "72"
Output:
1
 
Example 2:
Input:
7
Output:
0
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function checkDivisible36() which takes the string S and returns 1 is divisible by 36, else 0.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |S| <= 10^{5}
"""

def is_divisible_by_36(S: str) -> int:
    try:
        number = int(S)
        if number % 36 == 0:
            return 1
        else:
            return 0
    except ValueError:
        # If S cannot be converted to an integer, it's not a valid number
        return 0