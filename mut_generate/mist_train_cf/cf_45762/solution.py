"""
QUESTION:
Write two functions, `encode(num)` and `decode(encoded)`, where `encode(num)` takes a non-negative integer `num` and returns its encoding string, and `decode(encoded)` takes the encoded string and returns the original number. The encoding is done by converting the integer to a string, reversing the binary representation of the integer, and appending '1' at the end. The decoding function should reverse this process. The constraints are `0 <= num <= 10^9` for the encoding function and the input string for the decoding function will only contain '0' and '1', and its length will be between 1 and 30.
"""

def encode(num):
    binary = bin(num)[2:]  # convert number to binary string and strip off the '0b' at the start of the string
    return binary[::-1] + '1'  # reverse the binary string and add '1' to the end

def decode(encoded):
    return int(encoded[:-1][::-1], 2)  # remove '1' from the end, reverse the string, and convert back to a decimal number