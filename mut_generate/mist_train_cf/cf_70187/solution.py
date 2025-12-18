"""
QUESTION:
Design a function `check_pin(pin)` that takes a string input representing a user's access pin and returns "Valid" if the pin meets the following criteria, otherwise returns "Invalid":

- The pin has an odd number of digits.
- The pin contains at least two non-sequential numbers.
- The pin does not form any known number patterns (like "1234", "1111", etc. or their reverse like "4321" or "1111").
- The pin does not contain any two consecutive identical numbers.

The input pin should be taken as a string for simplicity.
"""

def check_pin(pin):
    # Check if pin has odd number of digits
    if len(pin) % 2 == 0:
        return "Invalid"
        
    # Check if pin doesn't have two non-sequential numbers
    if all(int(pin[i]) == int(pin[i-1])+1 or int(pin[i]) == int(pin[i-1])-1 
           for i in range(1, len(pin))):
        return "Invalid"
    
    # Check if pin doesn't form known patterns
    if all(pin[i] == pin[0] for i in range(len(pin))) or pin == pin[::-1] or pin == "1234" or pin == "4321":
        return "Invalid"

    # Check if pin doesn't have two consecutive identical numbers
    for i in range(len(pin)-1):
        if pin[i] == pin[i+1]:
            return "Invalid"
    
    return "Valid"