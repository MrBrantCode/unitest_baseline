"""
QUESTION:
Create a function `draw_unicorn(size, horn_length, mane_style, tail_style, char)` that generates and prints out an ASCII art of a unicorn with varying characteristics. The function should take in the following parameters: 

- `size`: An integer value between 1 and 5, where 1 represents the smallest size and 5 represents the largest size.
- `horn_length`: An integer value between 1 and 5, where 1 represents the shortest horn and 5 represents the longest horn.
- `mane_style`: A string, either "curly" or "straight", representing the mane's appearance.
- `tail_style`: A string, either "curly" or "straight", representing the tail's appearance.
- `char`: A custom character to represent the outline of the unicorn.

The function should return an error message if any of the inputs are invalid.
"""

def draw_unicorn(size, horn_length, mane_style, tail_style, char):
    # Check input validity
    if (not (isinstance(size, int) and 1<= size <= 5)) or (not (isinstance(horn_length, int) and 1<= horn_length <= 5)) or mane_style not in ['curly', 'straight'] or tail_style not in ['curly', 'straight'] or not isinstance(char, str):
        return 'Invalid input. Please try again with valid parameters.'

    # Convert parameters into ASCII characters
    if mane_style == 'curly':
        mane_char = '~'
    else:
        mane_char = '|'

    if tail_style == 'curly':
        tail_char = '~'
    else:
        tail_char = '|'

    # Draw the unicorn
    for i in range(size):
        print(char * horn_length + char * size)        # Draw the head and horn
        print(char * (horn_length + size) + mane_char) # Draw the body and mane
    print(char * (size + horn_length) + tail_char)      # Draw the tail