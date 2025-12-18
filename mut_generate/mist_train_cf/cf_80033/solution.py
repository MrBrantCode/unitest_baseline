"""
QUESTION:
Write a function `zigzag(text, n)` that takes a string `text` and an integer `n` as input, and prints the characters of the string in a zigzag pattern with `n` rows. If `n` is 1, simply print the string. If `n` is greater than 1, distribute the characters across the rows in a zigzag pattern, moving down when reaching the first row and up when reaching the last row.
"""

# Function to convert string into zigzag pattern
def zigzag(text, n):
    # Edge case - if number of rows is 1
    if n == 1:
        return text

    # Initialize an empty list to store each "zig-zag" line
    lines = ['' for _ in range(n)]
    
    # Define direction of zigzag
    down = False

    # Value to track which line in the zigzag we're currently on
    row = 0

    # Iterate over each character in the text
    for char in text:
        # Add this character to the current line
        lines[row] += char

        # If we've reached the first or last line, change direction
        if row == 0 or row == n - 1:
            down = not down

        # Depending on the direction, move up or down in the zigzag pattern
        if down:
            row += 1
        else:
            row -= 1

    # Finally, return the zigzag as a list of strings
    return lines