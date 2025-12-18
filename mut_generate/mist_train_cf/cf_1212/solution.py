"""
QUESTION:
Implement a function called `validate_isbn` that takes a string `isbn` as input and returns `True` if the ISBN number is valid, and `False` otherwise. An ISBN is valid if it consists of exactly 13 digits, its first three digits are either '978' or '979', and the sum of the products of each digit and its position (starting from 1) is divisible by 10. Additionally, consider an ISBN number valid if it passes a barcode validation, which checks if it starts with either '978' or '979'. The function should also keep track of previously used ISBN numbers and return `False` if the number has been used before.
"""

used_isbn_numbers = []

def validate_isbn(isbn):
    """
    Validate an ISBN number.
    
    Args:
        isbn (str): The ISBN number to validate.
    
    Returns:
        bool: True if the ISBN number is valid, False otherwise.
    """
    
    # Check length
    if len(isbn) != 13:
        return False
    
    # Check prefix
    prefix = isbn[:3]
    if prefix not in ['978', '979']:
        return False
    
    # Check digits
    if not isbn.isdigit():
        return False
    
    # Check uniqueness
    if isbn in used_isbn_numbers:
        return False
    else:
        used_isbn_numbers.append(isbn)
    
    # Calculate the sum of products of each digit and its position
    total = 0
    for i, digit in enumerate(isbn[:-1]):
        total += int(digit) * (i + 1)
    
    # Check if the total is divisible by 10
    if total % 10 != int(isbn[-1]):
        return False
    
    return True