"""
QUESTION:
-----Input-----

The only line of the input contains a string of digits. The length of the string is between 1 and 10, inclusive.


-----Output-----

Output "Yes" or "No".


-----Examples-----
Input
373

Output
Yes

Input
121

Output
No

Input
436

Output
Yes
"""

def is_special_palindrome(input_string: str) -> str:
    s = ['23', '10', '30', '11', '13', '12', '31', '33', '32', '21']
    ans = ''
    
    for x in input_string:
        ans += s[ord(x) - 48]
    
    if ans == ans[::-1]:
        return 'Yes'
    else:
        return 'No'