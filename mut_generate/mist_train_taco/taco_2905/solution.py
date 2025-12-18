"""
QUESTION:
Fans of The Wire will appreciate this one. 
For those that haven't seen the show, the Barksdale Organization has a simple method for encoding telephone numbers exchanged via pagers: "Jump to the other side of the 5 on the keypad, and swap 5's and 0's."

Here's a keypad for visualization.
```
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

Detective, we're hot on their trail! We have a big pile of encoded messages here to use as evidence, but it would take way too long to decode by hand. Could you write a program to do this for us?


Write a funciton called decode(). Given an encoded string, return the actual phone number in string form. Don't worry about input validation, parenthesies, or hyphens.
"""

def decode_phone_number(encoded_number: str) -> str:
    """
    Decodes an encoded phone number using the Barksdale Organization's method.

    The method involves jumping to the other side of the 5 on the keypad and swapping 5's and 0's.

    :param encoded_number: The encoded phone number string.
    :return: The decoded phone number string.
    """
    return encoded_number.translate(str.maketrans('1234567890', '9876043215'))