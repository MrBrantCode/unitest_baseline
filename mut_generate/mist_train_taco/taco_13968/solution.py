"""
QUESTION:
In this kata, you have to define a function named **func** that will take a list as input.

You must try and guess the pattern how we get the output number and return list - **[output number,binary representation,octal representation,hexadecimal representation]**, but **you must convert that specific number without built-in : bin,oct and hex functions.**

Examples : 

```python
func([12,13,6,3,6,45,123]) returns - [29,'11101','35','1d']

func([1,9,23,43,65,31,63,99]) returns - [41,'101001','51','29']

func([2,4,6,8,10,12,14,16,18,19]) returns - [10,'1010','12','a']
```
"""

def calculate_representations(l: list) -> list:
    # Calculate the average of the list using integer division
    n = sum(l) // len(l)
    
    # Convert the average to binary, octal, and hexadecimal without using built-in functions
    binary = convert_to_base(n, 2)
    octal = convert_to_base(n, 8)
    hexadecimal = convert_to_base(n, 16)
    
    # Return the result as a list
    return [n, binary, octal, hexadecimal]

def convert_to_base(n: int, base: int) -> str:
    # Helper function to convert a number to a given base without built-in functions
    if n == 0:
        return '0'
    
    digits = []
    while n:
        remainder = n % base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            # For hexadecimal, use letters A-F
            digits.append(chr(remainder - 10 + ord('a')))
        n //= base
    
    # Join the digits in reverse order
    return ''.join(digits[::-1])