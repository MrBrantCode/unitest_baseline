"""
QUESTION:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:


    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...


Example 1:


Input: 1
Output: "A"


Example 2:


Input: 28
Output: "AB"


Example 3:


Input: 701
Output: "ZY"
"""

def convert_to_excel_column(n: int) -> str:
    ans = ''
    while n > 0:
        n -= 1  # Adjust to 0-based index
        p = n % 26
        ans += chr(65 + p)  # Convert to corresponding letter
        n //= 26
    return ans[::-1]