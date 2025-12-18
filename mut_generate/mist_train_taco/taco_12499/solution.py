"""
QUESTION:
You all might have heard about hamming distance in Information Theory.

The Hamming distance between two strings of equal length is the number of positions at which the corresponding symbols are different. It measures the minimum number of errors that could have transformed one string into the other.

Given two integers we will define hamming distance between them as number of bits which are to be flipped in binary representation of a number to convert it into the other.
Example: Hamming distance between 4(100) and 5(101) is 1.
Note: Assume all the given integers are of 32 bits.

Input:
First line consists an integer t representing number of test cases.
Next t lines consists of 2 space separated integers x, y.

1 ≤ t ≤ 1000

0 ≤ x,y ≤ (2^30)

Output:
For each test case print out the answer in a new line.

SAMPLE INPUT
2
4 5
127 126

SAMPLE OUTPUT
1
1
"""

def calculate_hamming_distance(x: int, y: int) -> int:
    # Convert both integers to their binary representations
    bin_x = bin(x)[2:].zfill(32)
    bin_y = bin(y)[2:].zfill(32)
    
    # Calculate the Hamming distance
    hamming_distance = sum(bit_x != bit_y for bit_x, bit_y in zip(bin_x, bin_y))
    
    return hamming_distance