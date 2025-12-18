"""
QUESTION:
Create a function `largest_number(digits)` that takes a list of integers `digits` (1 <= len(digits) <= 10) and returns the largest number that can be formed by concatenating these digits, handling leading zeros properly.
"""

def largest_number(digits):
    # Convert each digit to a string for comparison during sorting
    digits = list(map(str, digits))
    
    # Custom sorting function to compare concatenated strings
    def compare(a, b):
        return int(b + a) - int(a + b)
    
    # Sort the digits using the custom comparison function
    digits.sort(key=functools.cmp_to_key(compare))
    
    # Join the sorted digits to form the largest number
    largest_num = ''.join(digits)
    
    return largest_num if largest_num[0] != '0' else '0'  # Handle case where the largest number is 0