"""
QUESTION:
# Convert Improper Fraction to Mixed Number

You will need to convert an [improper fraction](https://www.mathplacementreview.com/arithmetic/fractions.php#improper-fractions) to a [mixed number](https://www.mathplacementreview.com/arithmetic/fractions.php#mixed-number). For example:

```python
get_mixed_num('18/11') # Should return '1 7/11'
get_mixed_num('13/5') # Should return '2 3/5'
get_mixed_num('75/10') # Should return '7 5/10'
```

NOTE: All fractions will be greater than 0.
"""

def convert_improper_to_mixed(fraction: str) -> str:
    """
    Converts an improper fraction to a mixed number.

    Parameters:
    fraction (str): A string representing the improper fraction in the format "numerator/denominator".

    Returns:
    str: A string representing the mixed number in the format "whole_part numerator/denominator".
    """
    (numerator, denominator) = [int(i) for i in fraction.split('/')]
    whole_part = numerator // denominator
    remainder = numerator % denominator
    return f'{whole_part} {remainder}/{denominator}'