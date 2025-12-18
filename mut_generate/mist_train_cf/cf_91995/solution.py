"""
QUESTION:
Write a function named `romanToInt` that takes a string representing a Roman numeral as input and returns its corresponding integer value. The input string will only contain valid Roman numerals in uppercase and its length will be at most 15. The function should follow the standard rules of Roman numeral conversion.
"""

def romanToInt(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for i in range(len(s)):
        current_value = roman_values[s[i]]
        
        if current_value > prev_value:
            # Subtraction case: subtract the previous value and add the current value
            total += current_value - 2 * prev_value
        else:
            # Regular case: add the current value to the total
            total += current_value
        
        prev_value = current_value
    
    return total