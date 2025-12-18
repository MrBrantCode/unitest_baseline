"""
QUESTION:
You are given a string s consisting of `A`, `B` and `C`.

Snuke wants to perform the following operation on s as many times as possible:

* Choose a contiguous substring of s that reads `ABC` and replace it with `BCA`.



Find the maximum possible number of operations.

Constraints

* 1 \leq |s| \leq 200000
* Each character of s is `A`, `B` and `C`.

Input

Input is given from Standard Input in the following format:


s


Output

Find the maximum possible number of operations.

Examples

Input

ABCABC


Output

3


Input

C


Output

0


Input

ABCACCBABCBCAABCB


Output

6
"""

def max_operations_on_string(s: str) -> int:
    # Replace 'BC' with 'X' to simplify counting operations
    T = s.replace('BC', 'X')
    
    res = 0
    cnt = 0
    
    # Iterate through the transformed string T
    for char in T:
        if char == 'A':
            cnt += 1
        elif char == 'X':
            res += cnt
        else:
            cnt = 0
    
    return res