"""
QUESTION:
In mathematics, a **pandigital number** is a number that in a given base has among its significant digits each digit used in the base at least once. For example, 1234567890 is a pandigital number in base 10.

For simplification, in this kata, we will consider pandigital numbers in *base 10* and with all digits used *exactly once*. The challenge is to calculate a sorted sequence of pandigital numbers, starting at a certain `offset` and with a specified `size`.

Example:
```python
  > get_sequence(0, 5)
  [1023456789, 1023456798, 1023456879, 1023456897, 1023456978]
```

Rules:
- We are looking for positive pandigital numbers in base 10.
- Each digit should occur `exactly once`.
- A pandigital number can't start with digit zero.
- The offset is an integer (negative, zero or positive number) (long in Java)
- The size is a positive integer number (int in Java)
- Return the `size` pandigital numbers which are not smaller than the `offset`. If there is not enough `size` pandigital numbers, just return all of them.
- Return an empty array if nothing is found.
"""

def get_pandigital_sequence(offset, size):
    # Initialize the starting point for pandigital numbers
    start = 1023456789
    # Initialize the list to store pandigital numbers
    pandigital_numbers = []
    
    # Determine the actual starting point based on the offset
    if offset > 0 and offset > start:
        current = offset
    else:
        current = start
    
    # Loop through potential pandigital numbers
    while current <= 9876543210 and len(pandigital_numbers) < size:
        current_str = str(current)
        # Check if the number is pandigital
        if current_str[0] != '0' and len(set(current_str)) == 10:
            pandigital_numbers.append(current)
        current += 1
    
    return pandigital_numbers