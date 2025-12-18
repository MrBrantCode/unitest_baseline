"""
QUESTION:
Given few numbers, you need to print out the digits that are not being used.

Example:

```python
unused_digits(12, 34, 56, 78) # "09"
unused_digits(2015, 8, 26) # "3479"
```

Note:

- Result string should be sorted
- The test case won't pass Integer with leading zero
"""

def find_unused_digits(*args):
    # Convert all arguments to a single string of digits
    all_digits = ''.join(str(arg) for arg in args)
    
    # Create a set of all digits from '0' to '9'
    all_possible_digits = set('0123456789')
    
    # Create a set of digits used in the arguments
    used_digits = set(all_digits)
    
    # Find the unused digits by subtracting used digits from all possible digits
    unused_digits = all_possible_digits - used_digits
    
    # Convert the set of unused digits to a sorted string
    return ''.join(sorted(unused_digits))