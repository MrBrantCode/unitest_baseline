"""
QUESTION:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.
Example 1:
Input:
N = 28
Output: AB
Explanation: 1 to 26 are A to Z.
Then, 27 is AA and 28 = AB.
Ã¢â¬â¹Example 2:
Input: 
N = 13
Output: M
Explanation: M is the 13th character of
alphabet.
Your Task:
You don't need to read input or print anything. Your task is to complete the function colName() which takes the column number N as input and returns the column name represented as a string.
 
Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 4294967295
"""

def excel_column_title(n: int) -> str:
    """
    Converts a given column number to its corresponding Excel column title.

    Parameters:
    n (int): The column number.

    Returns:
    str: The corresponding Excel column title.
    """
    str1 = ''
    while n != 0:
        if n % 26 == 0:
            str1 = 'Z' + str1
            n = (n - 1) // 26
        else:
            str1 = chr(n % 26 - 1 + 65) + str1
            n = n // 26
    return str1