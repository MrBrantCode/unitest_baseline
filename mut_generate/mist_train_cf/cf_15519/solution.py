"""
QUESTION:
Create a function `create_array(n)` that generates an array of size `n` filled with the string "hello". Each string element in the array should have its vowels converted to uppercase, consonants to lowercase, and characters reversed. The function should return the modified array.
"""

def create_array(n):
    """
    Generates an array of size n filled with the string "hello". 
    Each string element in the array has its vowels converted to uppercase, 
    consonants to lowercase, and characters reversed.
    
    Args:
        n (int): The size of the array.
    
    Returns:
        list: A list of modified strings.
    """
    def convert_string(string):
        vowels = 'aeiou'
        result = ''
        for char in string:
            if char.lower() in vowels:
                result += char.upper()
            else:
                result += char.lower()
        return result
    
    return [convert_string("hello")[::-1] for _ in range(n)]