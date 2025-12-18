"""
QUESTION:
Write a function `compare_and_check_numbers` that takes two integers as input. It should return a string stating the larger number, whether it's even or odd, and whether it's divisible by 3. If both numbers are equal, it should also include a message stating so. The function should handle all possible cases, including equal numbers and numbers with different parity and divisibility by 3.
"""

def compare_and_check_numbers(a, b):
    if a > b:
        larger_num = a
        message = f"{a} is greater than {b}. "
    elif a < b:
        larger_num = b
        message = f"{b} is greater than {a}. "
    else:
        larger_num = a
        message = f"{a} and {b} are equal. "
        
    if larger_num % 2 == 0:
        parity_message = f"{larger_num} is an even number."
    else:
        parity_message = f"{larger_num} is an odd number."
        
    if larger_num % 3 == 0:
        divisibility_message = f"{larger_num} is divisible by 3."
    else:
        divisibility_message = f"{larger_num} is not divisible by 3."
        
    return message + parity_message + "\n" + divisibility_message