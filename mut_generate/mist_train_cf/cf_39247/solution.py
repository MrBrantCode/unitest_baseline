"""
QUESTION:
Implement a function `validate_cpf(cpf: str) -> bool` that takes a string representing a CPF number as input, removes non-numeric characters, and returns `True` if the resulting 11-digit number is valid according to the Brazilian CPF validation algorithm, and `False` otherwise.
"""

def validate_cpf(cpf: str) -> bool:
    cpf_digits = [int(digit) for digit in cpf if digit.isdigit()]
    
    if len(cpf_digits) != 11:
        return False
    
    # Calculate first verification digit
    sum_1 = sum([cpf_digits[i] * (10 - i) for i in range(9)])
    verification_digit_1 = 0 if sum_1 % 11 < 2 else 11 - (sum_1 % 11)
    
    if cpf_digits[9] != verification_digit_1:
        return False
    
    # Calculate second verification digit
    sum_2 = sum([cpf_digits[i] * (11 - i) for i in range(10)])
    verification_digit_2 = 0 if sum_2 % 11 < 2 else 11 - (sum_2 % 11)
    
    if cpf_digits[10] != verification_digit_2:
        return False
    
    return True