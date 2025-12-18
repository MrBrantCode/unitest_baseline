"""
QUESTION:
Write a function `validate_pin(pin)` that takes a string of digits `pin` and returns `True` if it meets the following conditions: 
- The number of digits in the pin is odd. 
- The pin contains at least two non-consecutive digits.
- The pin does not consist of the same digit repeated (e.g., '1111') and does not contain a universally recognized numeric sequence (e.g., '1234'). 
The function should return `False` otherwise.
"""

def validate_pin(pin):
    # Checking length is odd
    if len(pin) % 2 == 0:
        return False

    # Checking pin doesn't have all the same digits
    if len(set(pin)) == 1:
        return False

    # Checking pin has at least two non-consecutive digits
    non_consecutive = any(a != b for a, b in zip(pin, pin[1:]))
    if not non_consecutive:
        return False

    # Checking pin is not universally recognised sequence
    recognisable_seq = ['1234', '1111', '2222', '3333', '4444', 
                        '5555', '6666', '7777', '8888', '9999', '0000']
    if any(seq in pin for seq in recognisable_seq):
        return False

    # All checks passed
    return True