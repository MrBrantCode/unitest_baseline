"""
QUESTION:
## Nova polynomial add

This kata is from a series on polynomial handling. ( [#1](http://www.codewars.com/kata/nova-polynomial-1-add-1) [#2](http://www.codewars.com/kata/570eb07e127ad107270005fe) [#3](http://www.codewars.com/kata/5714041e8807940ff3001140 ) [#4](http://www.codewars.com/kata/571a2e2df24bdfd4e20001f5) )

Consider a polynomial in a list where each element in the list element corresponds to a factor. The factor order is the position in the list. The first element is the zero order factor (the constant).

`p = [a0, a1, a2, a3]` signifies the polynomial `a0 + a1x + a2x^2 + a3*x^3`

In this kata add two polynomials:

```python
poly_add ( [1, 2], [1] ) = [2, 2]
```
"""

def add_polynomials(p1, p2):
    # Ensure both polynomials are of the same length by padding with zeros
    max_len = max(len(p1), len(p2))
    p1 = p1 + [0] * (max_len - len(p1))
    p2 = p2 + [0] * (max_len - len(p2))
    
    # Add corresponding coefficients
    result = [p1[i] + p2[i] for i in range(max_len)]
    
    return result