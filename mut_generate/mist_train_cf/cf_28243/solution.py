"""
QUESTION:
Write two functions, `int_to_byte` and `byte_to_int`, to convert an integer to and from a byte array. 

The `int_to_byte` function should take three parameters: `num` (the integer to be converted), `num_bytes` (the number of bytes to represent the integer), and `byte_order` (the byte order, either 'big' or 'little'). It should return a byte array representing the input integer in the specified byte order.

The `byte_to_int` function should take a single parameter `b` (the byte array to be converted back to an integer) and return the integer value obtained by converting the byte array back. The `byte_to_int` function should assume the input byte array was created using the 'big' byte order.
"""

def int_to_bytes(num, num_bytes, byte_order):
    return num.to_bytes(num_bytes, byte_order)

def bytes_to_int(b):
    return int.from_bytes(b, byteorder='big', signed=False)