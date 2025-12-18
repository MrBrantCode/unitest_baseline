"""
QUESTION:
Write a function `find_narcissistic_numbers(n)` that takes an integer `n` as input and returns all narcissistic numbers less than or equal to `n`. A narcissistic number is the sum of its own digits each raised to the power of the number of digits. The function should return an error message if the input is not a non-negative integer.
"""

def find_narcissistic_numbers(n):
    # Check if the input is an integer and is positive
    if not isinstance(n, int) or n < 0:
        return 'Error: Input must be a non negative integer!'
    
    def is_narcissistic(num):
        # Convert the number to string to easily get the digits
        num_str = str(num)
        len_num = len(num_str)
        return num == sum(int(x)**len_num for x in num_str)
    
    # Use list comprehension to find all narcissistic nums
    narcissistic_nums = [i for i in range(abs(n)+1) if is_narcissistic(i)]
    
    return narcissistic_nums