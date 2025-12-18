"""
QUESTION:
Write a function `hexadecimal_XOR(num1, num2)` that computes the aggregate of the bitwise exclusive OR (XOR) operation performed on each individual digit of two hexadecimal numerals `num1` and `num2`. The function should accept two strings `num1` and `num2` as input, where each string represents a hexadecimal numeral. The function should return the aggregate of the XOR operation performed on each digit of the two input numerals.
"""

def hexadecimal_XOR(num1, num2):
    # Convert hexadecimal to binary
    bin1 = bin(int(num1, 16))[2:].zfill(4)
    bin2 = bin(int(num2, 16))[2:].zfill(4)

    # Perform XOR operation and aggregate the results
    aggregate = 0
    for b1, b2 in zip(bin1, bin2):
        xorResult = int(b1) ^ int(b2)
        aggregate += xorResult

    return aggregate