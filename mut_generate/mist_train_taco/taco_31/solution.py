"""
QUESTION:
# Solve For X

You will be given an equation as a string and you will need to [solve for X](https://www.mathplacementreview.com/algebra/basic-algebra.php#solve-for-a-variable) and return x's value. For example: 

```python
solve_for_x('x - 5 = 20') # should return 25
solve_for_x('20 = 5 * x - 5') # should return 5
solve_for_x('5 * x = x + 8') # should return 2
solve_for_x('(5 - 3) * x = x + 2') # should return 2
```

NOTES:
 * All numbers will be whole numbers
 * Don't forget about the [order of operations](https://www.mathplacementreview.com/algebra/basic-algebra.php#order-of-operations).
 * If the random tests don't pass the first time, just run them again.
"""

def solve_for_x(equation: str) -> int:
    from itertools import count
    
    # Iterate over positive and negative integers to find the value of x
    for n in count(0):
        for x in [n, -n]:
            # Replace 'x' with the current value of x and evaluate the equation
            if eval(equation.replace('x', str(x)).replace('=', '==')):
                return x