"""
QUESTION:
Given an input A , print the data type of the input A.
eg:-Sequence of digits -- int
      Sequence of digits with a dot -- float
      Sequence of chars  -- string
      Single non-digit char --- char
 
Example 1:
Input: A = "12"
Output: "int"
Explanation: The input consists only of
digits.
Example 2:
Input: A = "gfg"
Output: "string"
Explanation: The input consists only of
characters.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindInputType() which takes A as input parameter and returns data type of A.
 
Expected Time Complexity: O(|A|)
Expected Space Complexity: O(1)
 
Constraints:
1 <= |A| <= 1000
"""

def find_input_type(A: str) -> str:
    if A.isdigit():
        return 'int'
    if '.' in A:
        parts = A.split('.')
        if (len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()) or \
           (len(parts) == 2 and parts[0] == '' and parts[1].isdigit()):
            return 'float'
        elif len(A) > 1:
            return 'string'
    if len(A) == 1:
        return 'char'
    elif len(A) > 1:
        return 'string'