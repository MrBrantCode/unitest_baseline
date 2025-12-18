"""
QUESTION:
# Task
 Given an integer `n`, find the maximal number you can obtain by deleting exactly one digit of the given number.

# Example

 For `n = 152`, the output should be `52`;
 
 For `n = 1001`, the output should be `101`.
 
# Input/Output


 - `[input]` integer `n`

    Constraints: `10 ≤ n ≤ 1000000.`


 - `[output]` an integer
"""

def find_maximal_number_after_deletion(n: int) -> int:
    s = str(n)
    return int(max((s[:i] + s[i + 1:] for i in range(len(s)))))