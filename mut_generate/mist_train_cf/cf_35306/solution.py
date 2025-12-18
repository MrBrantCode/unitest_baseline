"""
QUESTION:
Implement the `binary_operation` function, which takes a string `binary_string` of binary digits as input. The function should iterate through the string, counting the occurrences of "0" and "1", and create a new string `new_line` where each character is "1" if the count of "1" is greater than the count of "0" encountered so far, and "0" otherwise. The function should then convert `new_line` to an integer using binary representation, create a reversed string by replacing "0" with "1" and "1" with "0" in `new_line`, convert the reversed string to an integer using binary representation, and return the product of the two integers. The function should return an integer.
"""

def binary_operation(binary_string: str) -> int:
    bzero = 0
    bone = 0
    new_line = ""

    for val in binary_string:
        if val == "0":
            bzero += 1
        else:
            bone += 1
        if bone > bzero:
            new_line += "1"
        else:
            new_line += "0"

    bin_value = int(new_line, 2)
    reversed_value = new_line.replace("0", "t").replace("1", "0").replace("t", "1")
    inverted = int(reversed_value, 2)
    return bin_value * inverted