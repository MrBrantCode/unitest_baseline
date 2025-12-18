"""
QUESTION:
Create a function named `print_sum_of_digits` that accepts a list of integers and prints out the sum of digits for each number in the list. The function should validate the input to ensure it is a list of integers. The length of the input list should be between 1 and 100, and each number in the list should be between 0 and 10^9. The solution should have a time complexity of O(n), where n is the total number of digits in the input list.
"""

def print_sum_of_digits(input_list):
    """
    This function accepts a list of integers, validates the input, 
    and prints out the sum of digits for each number in the list.
    
    Args:
        input_list (list): A list of integers.
        
    Returns:
        None
    """
    def get_sum_of_digits(num):
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits

    def validate_input(input_list):
        if not isinstance(input_list, list):
            return False
        if len(input_list) < 1 or len(input_list) > 100:
            return False
        for num in input_list:
            if not isinstance(num, int) or num < 0 or num > 10**9:
                return False
        return True

    if not validate_input(input_list):
        print("Invalid input. Please enter a list of integers.")
        return
    for num in input_list:
        sum_digits = get_sum_of_digits(num)
        print(f"Sum of digits for {num}: {sum_digits}")