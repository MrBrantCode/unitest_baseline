"""
QUESTION:
A binary gap within a positive number ```num``` is any sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of  ```num```. 
    For example:
    ```9``` has binary representation ```1001``` and contains a binary gap of length ```2```.
    ```529``` has binary representation ```1000010001``` and contains two binary gaps: one of length ```4``` and one of length ```3```.
    ```20``` has binary representation ```10100``` and contains one binary gap of length ```1```.
    ```15``` has binary representation ```1111``` and has ```0``` binary gaps.
    Write ```function gap(num)```
that,  given a positive ```num```,  returns the length of its longest binary gap. The function should return ```0``` if ```num``` doesn't contain a binary gap.
"""

def longest_binary_gap(num):
    # Convert the number to binary and remove the '0b' prefix
    binary_representation = bin(num)[2:]
    
    # Strip leading and trailing zeros to focus on gaps
    stripped_binary = binary_representation.strip('0')
    
    # Split the binary string by '1' to isolate the gaps of zeros
    gaps = stripped_binary.split('1')
    
    # Find the length of the longest gap
    longest_gap = max(len(gap) for gap in gaps)
    
    return longest_gap