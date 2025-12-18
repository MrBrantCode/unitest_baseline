"""
QUESTION:
# Write Number in Expanded Form - Part 2

This is version 2 of my ['Write Number in Exanded Form' Kata](https://www.codewars.com/kata/write-number-in-expanded-form).

You will be given a number and you will need to return it as a string in [Expanded Form](https://www.mathplacementreview.com/arithmetic/decimals.php#writing-a-decimal-in-expanded-form). For example:

```python
expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
expanded_form(0.04) # Should return '4/100'
```
"""

def expanded_form(num):
    # Split the number into integer and fractional parts
    integer_part, fractional_part = str(num).split('.')
    
    # Process the integer part
    integer_result = [str(int(digit) * 10 ** i) for i, digit in enumerate(integer_part[::-1]) if digit != '0'][::-1]
    
    # Process the fractional part
    fractional_result = [f"{digit}/{10 ** (i + 1)}" for i, digit in enumerate(fractional_part) if digit != '0']
    
    # Combine the results
    result = integer_result + fractional_result
    
    # Join the results with ' + ' and return
    return ' + '.join(result)