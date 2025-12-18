"""
QUESTION:
Design a function `check_pin(pin)` that validates a user's access pin. The pin is valid only if it meets the following conditions: 
- It has an odd number of digits.
- It contains at least two non-sequential numbers (i.e., the difference between consecutive digits is not constant).
- It does not contain any of the known number patterns (for this problem, the known patterns are '12345', '11111', '67890', '55555', '54321').
"""

import re

def check_pin(pin):
    # must have odd number of digits
    if len(pin) % 2 == 0:
        return False
    
    # must not form any known patterns
    known_patterns = ['12345', '11111', '67890', '55555', '54321']
    for pattern in known_patterns:
        if pattern in pin:
            return False
    
    # must have at least two non-sequential numbers
    if len(set(pin)) < 2:
        return False

    sequential = all(int(pin[i]) - int(pin[i-1]) == int(pin[i-1]) - int(pin[i-2]) for i in range(2, len(pin)))
    if sequential:
	    return False

    # if none of the above conditions are met, the pin is valid
    return True