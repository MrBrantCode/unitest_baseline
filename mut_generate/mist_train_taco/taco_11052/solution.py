"""
QUESTION:
Given two strings representing two complex numbers.


You need to return a string representing their multiplication. Note i2 = -1 according to the definition.


Example 1:

Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.



Example 2:

Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.



Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
"""

def multiply_complex_numbers(num1: str, num2: str) -> str:
    # Split the input strings into real and imaginary parts
    a1, b1 = num1.split('+')
    a2, b2 = num2.split('+')
    
    # Remove the 'i' from the imaginary parts
    b1 = b1[:-1]
    b2 = b2[:-1]
    
    # Convert the parts to integers
    a1, b1 = int(a1), int(b1)
    a2, b2 = int(a2), int(b2)
    
    # Calculate the real and imaginary parts of the product
    real_part = a1 * a2 - b1 * b2
    imag_part = b1 * a2 + a1 * b2
    
    # Return the result in the form "a+bi"
    return f"{real_part}+{imag_part}i"