"""
QUESTION:
# Write Number in Expanded Form

You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathplacementreview.com/arithmetic/whole-numbers.php#expanded-form). For example:

```python
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.

If you liked this kata, check out [part 2](https://www.codewars.com/kata/write-number-in-expanded-form-part-2)!!
"""

def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    expanded_components = [
        digit + '0' * (length - i - 1)
        for i, digit in enumerate(num_str)
        if digit != '0'
    ]
    return ' + '.join(expanded_components)