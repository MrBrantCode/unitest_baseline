"""
QUESTION:
The Ackermann function is a famous function that played a big role in computability theory as the first example of a total computable function that is not primitive recursive.

Since then the function has been a bit simplified but is still of good use. Due to its definition in terms of extremely deep recursion it can be used as a benchmark of a compiler's ability to optimize recursion. 

The goal of this kata is to code a function which will be given two inputs, m and n, and will return the Ackermann number A(m,n) defined by:

```
A(m,n) = n+1                          if m=0  
A(m,n) = A(m-1,1)                     if m>0 , n=0
A(m,n) = A(m-1,A(m,n-1))              if m,n > 0
```

m,n should be non-negative integers, the function should return null (Javascript), None (Python), or nil (Ruby) for other type, non-integer and negative numbers. In C, input is restricted to integer type.
"""

from numbers import Number

def ackermann(m, n):
    # Check if both m and n are numbers and non-negative integers
    if isinstance(m, Number) and isinstance(n, Number):
        if isinstance(m, int) and isinstance(n, int) and m >= 0 and n >= 0:
            return ackermann_aux(m, n)
    return None

def ackermann_aux(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_aux(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann_aux(m - 1, ackermann_aux(m, n - 1))