"""
QUESTION:
Replace all occurrences of 'x' with 'y' in a given string. Implement the replacement algorithm from scratch without using built-in string manipulation functions or regular expressions. The algorithm should have a time complexity of O(n), where n is the length of the string, and use only constant space.
"""

def replace_x_with_y(sentence):
    """
    Replaces all occurrences of 'x' with 'y' in the given sentence.
    
    Time complexity: O(n), where n is the length of the sentence.
    Space complexity: Constant space.
    """
    result = ""
    for ch in sentence:
        if ch == 'x':
            result += 'y'
        else:
            result += ch
    return result