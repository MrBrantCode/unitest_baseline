"""
QUESTION:
Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple (depending on the language), and the reduced fraction must be returned as an array/tuple:

```
input:   [numerator, denominator]
output:  [newNumerator, newDenominator]
example: [45, 120] --> [3, 8]
```

All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!
"""

from fractions import Fraction

def reduce_fraction(fraction):
    """
    Reduces a given fraction to its simplest form.

    Parameters:
    fraction (tuple or list): A tuple or list containing two integers, 
                              representing the numerator and denominator of the fraction.

    Returns:
    tuple: A tuple containing two integers, representing the reduced numerator and denominator.
    """
    t = Fraction(*fraction)
    return (t.numerator, t.denominator)