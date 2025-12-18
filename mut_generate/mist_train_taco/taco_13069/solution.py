"""
QUESTION:
You have been tasked with converting a number from base i (sqrt of -1) to base 10. 

Recall how bases are defined: 

    abcdef = a * 10^5 + b * 10^4 + c * 10^3 + d * 10^2 + e * 10^1 + f * 10^0

Base i follows then like this:

    ... i^4 + i^3 + i^2 + i^1 + i^0

The only numbers in any place will be 1 or 0
Examples:
  101 in base i would be:
    
      1 * i^2 + 0 * i^1 + 1*i^0 = -1 + 0 + 1 = 0
      
  10010 in base i would be:
    
      1*i^4 + 0 * i^3 + 0 * i^2 + 1 * i^1 + 0 * i^0 = 1 + -i = 1-i

You must take some number, n, in base i and convert it into a number in base 10, in the format of a 2x1 vector.

    [a,b] = a+b*i
    
The number will always be some combination of 0 and 1

In Python you will be given an integer.
In Javascript and C++ you will be given a string
"""

def convert_base_i_to_base_10(n: str) -> list:
    # Convert the string representation of the number to a list of integers in reverse order
    ds = list(map(int, reversed(n)))
    
    # Calculate the real part: sum of every 4th element starting from index 0 minus sum of every 4th element starting from index 2
    real_part = sum(ds[::4]) - sum(ds[2::4])
    
    # Calculate the imaginary part: sum of every 4th element starting from index 1 minus sum of every 4th element starting from index 3
    imaginary_part = sum(ds[1::4]) - sum(ds[3::4])
    
    # Return the result as a list [real_part, imaginary_part]
    return [real_part, imaginary_part]