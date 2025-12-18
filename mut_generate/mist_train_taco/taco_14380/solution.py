"""
QUESTION:
Given a string S that represents column title of an Excel sheet, find the number that represents that column.
In excel A column is number 1, AA is 27 and so on. 
Example 1:
Input:
S = A
Output: 1
Example 2:
Input:
S = AA
Output: 27
Your Task:
Complete the function ExcelColumnNumber() which takes a string as input and returns an integer.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| <=7
"""

def excel_column_number(s: str) -> int:
    res = 0
    mul = 1
    for char in reversed(s):
        res += (ord(char) - 64) * mul
        mul *= 26
    return res