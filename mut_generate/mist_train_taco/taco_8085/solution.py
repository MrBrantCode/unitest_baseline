"""
QUESTION:
ABCXYZ company has up to 100 employees. 

The company decides to create a unique identification number (UID) for each of its employees. 

The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:  

It must contain at least $2$ uppercase English alphabet characters.   
It must contain at least $3$ digits ($\mbox{0}$ - $\mbox{9}$).  
It should only contain alphanumeric characters ($\boldsymbol{a}$ - $z$, $\mbox{A}$ - $\mbox{Z}$ & $\mbox{0}$ - $\mbox{9}$).  
No character should repeat.  
There must be exactly $10$ characters in a valid UID.

Input Format

The first line contains an integer $\mathbf{T}$, the number of test cases. 

The next $\mathbf{T}$ lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid

Explanation

B1CD102354: $\mbox{1}$ is repeating →  Invalid 

B1CDEF2354: Valid
"""

import re

def validate_uid(uid: str) -> str:
    regex_for_valid_uid_ignoring_repeats = re.compile('^(?=(.*?[a-zA-Z]){2})(?=(.*?\\d){3})(?:[a-zA-Z0-9]{10})$')
    regex_for_no_repeats = re.compile('^(?:([A-Za-z0-9])(?!.*\\1))+$')
    
    if regex_for_valid_uid_ignoring_repeats.match(uid) and regex_for_no_repeats.match(uid):
        return 'Valid'
    else:
        return 'Invalid'