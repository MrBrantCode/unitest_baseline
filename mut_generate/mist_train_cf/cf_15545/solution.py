"""
QUESTION:
Write a function called `calculate_sum` that takes a string of numbers separated by commas and returns the sum of all the numbers. The input string may contain negative numbers, floating-point numbers, numbers enclosed in parentheses, spaces between the numbers and commas, and invalid characters such as letters or special symbols that should be ignored.
"""

def calculate_sum(string):
    numbers = string.split(",")
    total_sum = 0
    
    for num in numbers:
        try:
            cleaned_num = ''.join(filter(lambda x: x.isdigit() or x in ['-', '.', '(', ')'], num.strip()))
            
            if cleaned_num.startswith("(") and cleaned_num.endswith(")"):
                cleaned_num = cleaned_num[1:-1]
            
            total_sum += float(cleaned_num)
        except ValueError:
            pass
    
    return total_sum