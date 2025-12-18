"""
QUESTION:
Create a hash function with a unique name, `calculate_string_hash`, that takes a string `input_string` as input and returns a unique hash value. The hash function should use a prime number algorithm to generate hash values for each character in the string, handle Unicode characters, and produce evenly distributed hash values to minimize collisions. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1). The function should also be able to handle strings with collisions and combine the individual hash values of each character using a combination function, such as XOR or addition.
"""

def calculate_string_hash(input_string):
    """
    This function calculates a unique hash value for the input string using a prime number algorithm.
    
    Args:
    input_string (str): The input string for which the hash value is to be calculated.
    
    Returns:
    int: A unique hash value for the input string.
    """
    prime = 31  # Prime number used for hashing
    hash_value = 0
    
    for char in input_string:
        # Get the Unicode code point of the character
        char_hash = ord(char)
        
        # Ensure evenly distributed hash values
        char_hash = (char_hash * prime) % (2**32)
        
        # Combine the hash values using XOR
        hash_value ^= char_hash
    
    return hash_value