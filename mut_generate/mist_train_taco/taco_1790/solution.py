"""
QUESTION:
Adding tip to a restaurant bill in a graceful way can be tricky, thats why you need make a function for it.

The function will receive the restaurant bill (always a positive number) as an argument. You need to 1) **add at least 15%** in tip, 2) round that number up to an *elegant* value and 3) return it.

What is an *elegant* number? It depends on the magnitude of the number to be rounded. Numbers below 10 should simply be rounded to whole numbers. Numbers 10 and above should be rounded like this:

10 - 99.99... ---> Round to number divisible by 5

100 - 999.99... ---> Round to number divisible by 50

1000 - 9999.99... ---> Round to number divisible by 500

And so on...

Good luck!

## Examples
```
 1  -->    2
 7  -->    9
12  -->   15
86  -->  100
```
"""

from math import ceil, log10

def graceful_tipping(bill):
    # Step 1: Add at least 15% tip to the bill
    bill *= 1.15
    
    # Step 2: Determine the appropriate rounding unit based on the magnitude of the bill
    if bill < 10:
        # Round to the nearest whole number
        return ceil(bill)
    else:
        # Calculate the exponent of the bill
        e = int(log10(bill))
        # Determine the rounding unit based on the exponent
        unit = 10 ** e / 2
        # Round the bill to the nearest multiple of the rounding unit
        return ceil(bill / unit) * unit