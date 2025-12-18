"""
QUESTION:
Write a function named `count_occurrences` that takes a string and a character as input. The function should count the number of occurrences of the character in the string, excluding those within parentheses and square brackets, and only if they are not preceded or followed by another instance of the same character. The function should be case-sensitive.
"""

def count_occurrences(string, char):
    count = 0
    is_same_char = False
    ignore_brackets = False
    ignore_parentheses = False
    
    for i in range(len(string)):
        # Check if the character is within parentheses or square brackets
        if string[i] == '(':
            ignore_parentheses = True
        elif string[i] == ')':
            ignore_parentheses = False
        elif string[i] == '[':
            ignore_brackets = True
        elif string[i] == ']':
            ignore_brackets = False
            
        # Check if the character is the same as the previous one
        if string[i] == char:
            if i > 0 and string[i-1] == char:
                is_same_char = True
            elif i < len(string)-1 and string[i+1] == char:
                is_same_char = True
            else:
                # Check if the character is not within parentheses or square brackets
                if not ignore_parentheses and not ignore_brackets:
                    count += 1
                is_same_char = False
    
    return count