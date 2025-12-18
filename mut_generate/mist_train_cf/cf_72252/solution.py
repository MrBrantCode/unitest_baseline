"""
QUESTION:
Create a function `binary_to_unicode(binary_str, bit_endianness)` that converts a provided binary code into its corresponding Unicode symbol(s) and returns the result as a string. The input `binary_str` is a sequence of multiple binary values separated by spaces. The function should handle each binary value separately and raise a custom exception if any binary value is not a valid Unicode. The `bit_endianness` parameter specifies the byte order, either 'big' or 'little', defaulting to 'big' if not provided.
"""

class InvalidUnicodeException(Exception):
    def __init__(self, error):
        super().__init__(error)

def binary_to_unicode(binary_str, bit_endianness='big'):
    """
    Converts a provided binary code into its corresponding Unicode symbol(s) 
    and returns the result as a string.

    Args:
    binary_str (str): A sequence of multiple binary values separated by spaces.
    bit_endianness (str): The byte order, either 'big' or 'little'. Defaults to 'big'.

    Returns:
    str: The corresponding Unicode symbol(s) as a string.

    Raises:
    InvalidUnicodeException: If any binary value is not a valid Unicode.
    """

    binaries = binary_str.split()
    unicode_str = ""

    for binary in binaries:
        try:
            if bit_endianness == 'big':
                unicode_str += chr(int(binary, 2))
            else:
                unicode_str += chr(int(binary[::-1], 2))
        except ValueError as e:
            raise InvalidUnicodeException(f"Invalid unicode value: {binary}") from e
        
    return unicode_str