"""
QUESTION:
Write
```python
function repeating_fractions(numerator, denominator)
```
that given two numbers representing the numerator and denominator of a fraction, return the fraction in string format. If the fractional part has repeated digits, replace those digits with a single digit in parentheses. 

For example:
```python
repeating_fractions(1,1) === '1'
repeating_fractions(1,3) === '0.(3)'
repeating_fractions(2,888) === '0.(0)(2)5(2)5(2)5(2)5(2)5(2)'
```
"""

import re

def repeating_fractions(numerator, denominator):
    # Calculate the division and split into integer and decimal parts
    (integer_part, decimal_part) = str(numerator * 1.0 / denominator).split('.')
    
    # Replace repeating digits with a single digit in parentheses
    formatted_decimal_part = re.sub(r'([0-9])\1+', r'(\1)', decimal_part)
    
    # Combine integer and formatted decimal parts
    return integer_part + '.' + formatted_decimal_part