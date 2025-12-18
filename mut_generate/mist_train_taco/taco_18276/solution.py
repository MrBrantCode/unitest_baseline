"""
QUESTION:
Given an integer `n`, find two integers `a` and `b` such that:
```Pearl
A) a >= 0 and b >= 0
B) a + b = n
C) DigitSum(a) + Digitsum(b) is maximum of all possibilities.  
```
You will return the digitSum(a) + digitsum(b). 

```
For example:
solve(29) = 11. If we take 15 + 14 = 29 and digitSum = 1 + 5 + 1 + 4 = 11. There is no larger outcome.
```
`n` will not exceed `10e10`.

More examples in test cases. 

Good luck!
"""

def maximize_digit_sum(n: int) -> int:
    if n < 10:
        return n
    
    # Calculate the largest possible `a` that is a sequence of 9s
    a = int((len(str(n)) - 1) * '9')
    b = n - a
    
    # Calculate the sum of digits of `a` and `b`
    digit_sum = sum([int(i) for i in list(str(a)) + list(str(b))])
    
    return digit_sum