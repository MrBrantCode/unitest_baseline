"""
QUESTION:
Write a function `find_divisible_pair` that takes a list of decimal digits and a quotient as input. The function should return a pair of unique digits from the list such that the division of one digit by the other equals the given quotient. If no such pair exists, the function should return None.
"""

def find_divisible_pair(digits, quotient):
    """
    This function takes a list of decimal digits and a quotient as input.
    It returns a pair of unique digits from the list such that the division of one digit by the other equals the given quotient.
    If no such pair exists, the function returns None.
    """
    # First, we sort the list of digits in ascending order
    digits.sort()
    
    # We iterate over each digit in the sorted list
    for i in range(len(digits)):
        # For each digit, we iterate over the remaining digits in the list
        for j in range(i + 1, len(digits)):
            # We check if the current digit is not zero and the division of the current digit by the other digit equals the given quotient
            if digits[j] != 0 and digits[i] % digits[j] == 0 and digits[i] // digits[j] == quotient:
                # If the condition is met, we return the pair of digits
                return (digits[i], digits[j])
            # We also check if the other digit is not zero and the division of the other digit by the current digit equals the given quotient
            elif digits[i] != 0 and digits[j] % digits[i] == 0 and digits[j] // digits[i] == quotient:
                # If the condition is met, we return the pair of digits
                return (digits[j], digits[i])
    # If no pair of digits meets the condition, we return None
    return None