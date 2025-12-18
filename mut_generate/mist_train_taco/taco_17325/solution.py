"""
QUESTION:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.


Example: 

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

def longest_palindrome_length(s: str) -> int:
    re = 0
    set_s = set(s)
    flag = False
    
    for x in set_s:
        count_x = s.count(x)
        if count_x % 2 == 0:
            re += count_x
        elif count_x >= 3:
            re += count_x - 1
            flag = True
        elif count_x == 1:
            flag = True
    
    if flag:
        re += 1
    
    return re