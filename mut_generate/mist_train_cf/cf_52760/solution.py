"""
QUESTION:
Write a function `authenticate_pin(pin)` that takes an integer as input and returns `True` if the pin is valid and `False` otherwise. The pin is considered valid if it meets the following conditions: 
- it has an odd length, 
- it contains at least two non-ordered, non-consecutive digits, 
- and it does not contain any common numeric sequences (for this purpose, '1234' and '1111' are considered common sequences).
"""

def authenticate_pin(pin):
    # Common sequences
    common_sequences = ['1234', '1111']

    # Convert pin to string for easier manipulation
    pin = str(pin)

    # Check for length
    if len(pin) % 2 == 0:
        return False
    
    # Check for two non-ordered, nonconsecutive digits
    non_consecutive = [pin[i] for i in range(len(pin)-1) if pin[i+1] != str(int(pin[i])+1)]
    if len(non_consecutive) < 2:
        return False

    # Check if it resembles any common numeric sequences
    for seq in common_sequences:
        if seq in pin:
            return False

    # If none of the conditions fail, authentication is successful
    return True