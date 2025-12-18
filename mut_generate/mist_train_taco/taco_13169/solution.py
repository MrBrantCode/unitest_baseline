"""
QUESTION:
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
 
Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Example 3:
Input: n = 123456789
Output: "123.456.789"

Example 4:
Input: n = 0
Output: "0"

 
Constraints:

0 <= n < 2^31
"""

def add_thousands_separator(n: int) -> str:
    arr = []
    count = 0
    num = str(n)
    
    # Traverse the string from the end to the beginning
    for i in range(len(num) - 1, -1, -1):
        if count == 3:
            arr.append('.')
            count = 0
        arr.append(num[i])
        count += 1
    
    # Reverse the array and join to form the final string
    return ''.join(arr[::-1])