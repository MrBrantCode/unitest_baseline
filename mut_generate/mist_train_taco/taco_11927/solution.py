"""
QUESTION:
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.



Example 1:

Input: "owoztneoer"

Output: "012"



Example 2:

Input: "fviefuro"

Output: "45"
"""

def original_digits(s: str) -> str:
    dmap = {}
    dmap[0] = s.count('z')
    dmap[2] = s.count('w')
    dmap[4] = s.count('u')
    dmap[6] = s.count('x')
    dmap[8] = s.count('g')
    dmap[1] = s.count('o') - dmap[0] - dmap[2] - dmap[4]
    dmap[3] = s.count('h') - dmap[8]
    dmap[5] = s.count('f') - dmap[4]
    dmap[7] = s.count('s') - dmap[6]
    dmap[9] = s.count('i') - dmap[6] - dmap[8] - dmap[5]
    
    res = ''
    dmap = sorted(list(dmap.items()), key=lambda x: x[0])
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(lst)):
        res += lst[i] * dmap[i][1]
    
    return res