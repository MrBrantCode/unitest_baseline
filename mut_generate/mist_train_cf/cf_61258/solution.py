"""
QUESTION:
Implement a function named `alternate_reverse(chain)` that rearranges a given string of alphanumeric characters so that every alternate character is in reverse order from its original place. The input `chain` is a non-empty string of alphanumeric characters. The function should return a string with the rearranged characters.
"""

def alternate_reverse(chain):
    # Break down the chain into list of characters
    characters = list(chain)
    
    # Split into even and odd indexed characters
    even_chars = characters[::2]
    odd_chars = characters[1::2]
    
    # Reverse the odd indexed characters
    odd_chars = odd_chars[::-1]
    
    # Merge the lists
    result = [None]*(len(even_chars)+len(odd_chars))
    result[::2] = even_chars
    result[1::2] = odd_chars
    
    # Convert list back into string
    result = ''.join(result)
    return result