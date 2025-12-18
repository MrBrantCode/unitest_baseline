"""
QUESTION:
Having two standards for a keypad layout is inconvenient!  
Computer keypad's layout:  


 
Cell phone keypad's layout:  


Solve the horror of unstandartized keypads by providing a function that converts computer input to a number as if it was typed by a phone.

Example:  
"789" -> "123"

Notes:  
You get a string with numbers only
"""

def convert_computer_to_phone_keypad(computer_input: str) -> str:
    """
    Converts a string of numbers from a computer keypad layout to a phone keypad layout.

    :param computer_input: A string of numbers representing the computer keypad input.
    :return: A string representing the equivalent numbers on a phone keypad.
    """
    # Mapping from computer keypad to phone keypad
    keypad_map = {
        '0': '0', '1': '7', '2': '8', '3': '9',
        '4': '4', '5': '5', '6': '6', '7': '1',
        '8': '2', '9': '3'
    }
    
    # Convert each character in the input string using the keypad_map
    phone_output = ''.join(keypad_map[char] for char in computer_input)
    
    return phone_output