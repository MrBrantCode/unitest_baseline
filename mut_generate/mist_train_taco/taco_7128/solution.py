"""
QUESTION:
## Problem

Determine whether a positive integer number is **colorful** or not.

`263` is a colorful number because `[2, 6, 3, 2*6, 6*3, 2*6*3]` are all different; whereas `236` is not colorful, because `[2, 3, 6, 2*3, 3*6, 2*3*6]` have `6` twice.

So take all consecutive subsets of digits, take their product and ensure all the products are different.

## Examples
```pyhton
263  -->  true
236  -->  false
```
"""

def is_colorful(number):
    # Convert the number to a string to easily access individual digits
    num_str = str(number)
    
    # Initialize a list to store all products of consecutive subsets
    products = []
    
    # Collect individual digits
    for digit in num_str:
        products.append(int(digit))
    
    # Collect products of all consecutive pairs of digits
    for i in range(len(num_str) - 1):
        product = int(num_str[i]) * int(num_str[i + 1])
        products.append(product)
    
    # Collect the product of all digits (if more than one digit)
    if len(num_str) > 1:
        product = 1
        for digit in num_str:
            product *= int(digit)
        products.append(product)
    
    # Check if all products are unique
    return len(set(products)) == len(products)