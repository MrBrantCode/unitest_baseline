"""
QUESTION:
Given a string of form x + a = b where a and b are integer, find value of x [Note that spaces may or may not be there, for example, input can either be x+a=b or x + a = b or x+a = b]. 
For example if input string is x + 12 = 3 then output should be -9
 
Example 1:
Input: str = "x+5=2"
Output: -3
Explanation: 2 - 5 = -3
Example 2:
Input: str = "x+10=20"
Output: 10
Explanation: 20 - 10 = 10
 
Your Task:
You don't need to read or print anything. Your task is to complete the function solve() which takes the string str as input parameter and returns the value of the x.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1) 
 
Constraints:
1 <= a, b <= 1000
"""

def solve(str):
    # Remove any spaces from the input string
    str = str.replace(" ", "")
    
    # Split the string into two parts: left side and right side of the equation
    left_side, right_side = str.split('=')
    
    # Convert the right side to an integer
    b = int(right_side)
    
    # Split the left side by '+' to separate 'x' and 'a'
    x_part, a_part = left_side.split('+')
    
    # Convert 'a' to an integer
    a = int(a_part)
    
    # Calculate the value of x
    x = b - a
    
    return x