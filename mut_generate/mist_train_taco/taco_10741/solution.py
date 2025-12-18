"""
QUESTION:
Here you have to do some mathematical operations on a "dirty string". This kata checks some basics, it's not too difficult.


__So what to do?__

Input: String which consists of two positive numbers (doubles) and exactly one operator like `+, -, * or /` always between these numbers. The string is dirty, which means that there are different characters inside too, not only numbers and the operator. You have to combine all digits left and right, perhaps with "." inside (doubles), and to calculate the result which has to be rounded to an integer and converted to a string at the end.

### Easy example:

```
Input: "gdfgdf234dg54gf*23oP42"
Output: "54929268" (because 23454*2342=54929268)
```

First there are some static tests, later on random tests too...

### Hope you have fun! :-)
"""

import re

def calculate_string(st):
    # Remove all characters except digits, decimal points, and operators
    cleaned_string = re.sub('[^-+*/\\d.]', '', st)
    
    # Evaluate the cleaned string as a mathematical expression
    result = eval(cleaned_string)
    
    # Round the result to the nearest integer and convert to string
    return str(int(round(result)))