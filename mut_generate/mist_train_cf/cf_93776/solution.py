"""
QUESTION:
Write a function named `calculate_sum` that takes a string of comma-separated numbers as input. The string may contain negative numbers, floating-point numbers, numbers enclosed in parentheses, and invalid characters. The function should return the sum of all valid numbers, ignoring any invalid characters and numbers that cannot be converted to a float.
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