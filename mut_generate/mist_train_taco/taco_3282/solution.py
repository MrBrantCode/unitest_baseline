"""
QUESTION:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but **exactly** 4 digits or exactly 6 digits. 

If the function is passed a valid PIN string, return `true`, else return `false`.

## Examples 
```
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
```
"""

def validate_pin(pin: str) -> bool:
    """
    Validates whether the given PIN code is exactly 4 or 6 digits long and contains only digits.

    Parameters:
    pin (str): The PIN code to be validated.

    Returns:
    bool: True if the PIN code is valid, False otherwise.
    """
    return len(pin) in (4, 6) and pin.isdigit()