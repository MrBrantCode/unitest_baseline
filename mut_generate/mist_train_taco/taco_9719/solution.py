"""
QUESTION:
Write a function that removes every lone 9 that is inbetween 7s.

```python
seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'
```

Input: String
Output: String
"""

def remove_lone_nines_between_sevens(input_str):
    while '797' in input_str:
        input_str = input_str.replace('797', '77')
    return input_str