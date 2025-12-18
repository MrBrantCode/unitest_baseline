"""
QUESTION:
Implement a function named `reverse_and_count_consonants` that takes a string `s` as input, reverses the string using a stack without any built-in reverse functions, and returns the reversed string along with the count of consonants in the reversed string. The function should not use any built-in string reversal methods and should consider only alphabetic characters when counting consonants, ignoring case.
"""

def reverse_and_count_consonants(s):
    """
    Reverses the input string using a stack without any built-in reverse functions and returns the reversed string along with the count of consonants in the reversed string.

    Args:
        s (str): The input string.

    Returns:
        tuple: A tuple containing the reversed string and the count of consonants in the reversed string.
    """
    class Stack:
        def __init__(self):
            self.stack = []
        
        def push(self, item):
            self.stack.append(item)
        
        def pop(self):
            return self.stack.pop()
        
        def is_empty(self):
            return len(self.stack) == 0


    stack = Stack()
    for char in s:
        stack.push(char)
    
    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()
    
    consonant_count = len([char for char in reverse if char.lower() in 'bcdfghjklmnpqrstvwxyz'])
    
    return reverse, consonant_count