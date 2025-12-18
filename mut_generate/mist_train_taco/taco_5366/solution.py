"""
QUESTION:
Given two numbers (m and n) :

- convert all numbers from m to n to binary
- sum them as if they were in base 10 
- convert the result to binary
- return as string

Eg: with the numbers 1 and 4


   1 // 1 to binary is 1
+ 10 // 2 to binary is 10
+ 11 // 3 to binary is 11
+100 // 4 to binary is 100
----
 122 // 122 in Base 10 to Binary is 1111010



So BinaryPyramid ( 1 , 4 ) should return "1111010" 

range should be ascending in order
"""

def binary_pyramid(m: int, n: int) -> str:
    """
    Converts all numbers from m to n to binary, sums them as if they were in base 10,
    converts the result to binary, and returns it as a string.

    Parameters:
    - m (int): The starting number.
    - n (int): The ending number.

    Returns:
    - str: The binary representation of the sum of binary conversions of numbers from m to n.
    """
    return bin(sum((int(bin(i)[2:]) for i in range(m, n + 1))))[2:]