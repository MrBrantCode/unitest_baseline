"""
QUESTION:
A string is said to be "SUPER STRING" if the number of times the character appeared in the string is equal to its ASCII value. Given the conditions that the ASCII value of ‘a’ is 26 and z is ‘1’.

Input 

First line takes number of test cases ‘N’.
Following ‘N’ lines take string as input.

Output

‘Yes’ if the string is a super String
‘No’ if string is not a Super String

SAMPLE INPUT
2
ZYY
ZYYZ

SAMPLE OUTPUT
Yes
No

Explanation

'Z' appeared once and 'Y' appeared twice in the first test case so it was a 'Yes' and in second test case 'Z' appeared twice therefore it was a 'No'
"""

import string

def is_super_string(s: str) -> str:
    # Create a dictionary to map uppercase characters to their ASCII values
    d = {}
    j = 26
    for x in string.ascii_uppercase:
        d[x] = j
        j -= 1
    
    # Create a dictionary to count the frequency of each character in the string
    d1 = {}
    for x in s:
        d1[x] = d1.get(x, 0) + 1
    
    # Check if the frequency of each character matches its ASCII value
    count = 0
    for x in d1.keys():
        if d1[x] == d[x]:
            count += 1
    
    # Determine if the string is a super string
    if count == len(d1.keys()):
        return 'Yes'
    else:
        return 'No'