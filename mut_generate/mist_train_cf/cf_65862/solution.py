"""
QUESTION:
Write a function called "recovery_sequence" that takes a 2D list of binary digits and an integer representing the target remainder when the binary digits are divided by a divisor. The function should return the first sequence of consecutive binary digits that when converted to decimal and divided by the divisor, equals the target remainder.
"""

def recovery_sequence(matrix, divisor, target_remainder):
    """
    This function takes a 2D list of binary digits and an integer representing 
    the target remainder when the binary digits are divided by a divisor. It 
    returns the first sequence of consecutive binary digits that when converted 
    to decimal and divided by the divisor, equals the target remainder.
    """
    # Flatten the 2D list into a 1D list
    flat_list = [item for sublist in matrix for item in sublist]
    
    # Initialize variables to keep track of the current sequence and its decimal value
    sequence = ''
    decimal_value = 0
    
    # Iterate over the binary digits
    for digit in flat_list:
        # Add the current digit to the sequence
        sequence += digit
        
        # Update the decimal value
        decimal_value = int(sequence, 2)
        
        # Check if the decimal value divided by the divisor equals the target remainder
        if decimal_value % divisor == target_remainder:
            return sequence