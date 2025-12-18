"""
QUESTION:
Write a function `remove_even_and_sort_desc` that takes an integer `n` as input, removes any even digits from the number, and returns the remaining odd digits in descending order. The function should handle edge cases such as negative integers and zero without using the built-in sort function. The sign of the output number should be the same as the input number.
"""

def remove_even_and_sort_desc(n):
    # Convert the number into string
    str_num = str(n)
    
    # Check if n is negative and remove minus sign
    if str_num[0] == '-':
        str_num = str_num[1:]
    
    # Remove even digits
    str_num = ''.join([digit for digit in str_num if int(digit) % 2])
    
    # If n is zero or all digits are even (the string is empty after removing)
    if not str_num:
        return 0
    
    # Sort the remaining odd digits in descending order without using sort()
    sorted_str_num = ""
    for num in range(9, -1, -2):  # start from 9 to 1, step = -2
        sorted_str_num += str_num.count(str(num)) * str(num)
    
    # Returned the number after being processed
    return int(sorted_str_num) if n >= 0 else -int(sorted_str_num)