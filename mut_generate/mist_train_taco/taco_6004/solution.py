"""
QUESTION:
Given a positive integer N, return its corresponding column title as it would appear in an Excel sheet.
For N =1 we have column A, for 27 we have AA and so on.
Note: The alphabets are all in uppercase.
Example 1:
Input:
N = 51
Output: AY
Your Task:
Complete the function ExcelColumn() which takes N as input and returns output string.
Expected Time Complexity: O(Log(N))
Expected Auxiliary Space: O(Log(N))
Constraints:
1 ≤ N ≤ 10^{7}
"""

def excel_column_title(N: int) -> str:
    temp = N
    st = ''
    while temp:
        lt = temp % 26
        if lt == 0:
            st = 'Z' + st
            temp = temp // 26 - 1
        else:
            st = chr(64 + lt) + st
            temp = temp // 26
    return st