"""
QUESTION:
Write a function `is_narcissistic` that determines if a given integer `n` is a Narcissistic number or not. The input integer `n` will always be within the range of 1 to 10^9. The function should have a time complexity of O(log(n)) and a space complexity of O(1). A Narcissistic number is a number that is the sum of the nth power of each digit, where n is the number of digits in the number.
"""

def is_narcissistic(n):
    """
    Determines if a given integer is a Narcissistic number or not.
    
    A Narcissistic number is a number that is the sum of the nth power of each digit, 
    where n is the number of digits in the number.
    
    Args:
        n (int): The input integer to check.
    
    Returns:
        bool: True if the number is Narcissistic, False otherwise.
    """
    
    # Initialize a variable with the given integer
    num = n
    
    # Initialize a variable to keep track of the number of digits in num
    digit_count = 0
    
    # Count the number of digits in num
    while num > 0:
        digit_count += 1
        num //= 10
    
    # Set num back to the given integer
    num = n
    
    # Initialize a variable to store the sum of the nth power of each digit
    total_sum = 0
    
    # Calculate the sum of the nth power of each digit
    while num > 0:
        # Extract the last digit of num
        digit = num % 10
        
        # Raise the extracted digit to the power of digit_count and add it to total_sum
        total_sum += digit ** digit_count
        
        # Divide num by 10 to remove the last digit
        num //= 10
    
    # Check if total_sum is equal to the given integer
    return total_sum == n