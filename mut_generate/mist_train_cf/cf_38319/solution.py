"""
QUESTION:
Implement the function `add_text_to_matrix(matrix, text, font, position)` that takes a 32x32 LED matrix `matrix` as a 2D list of lists, a string `text` to display, a font `font` for the text, and a position `position` as a tuple `(x, y)` representing the top-left corner of the text on the matrix. The function should modify the LED matrix to display the given text at the specified position using the provided font, ensuring that the text is displayed within the bounds of the LED matrix and handle any overflow appropriately. The font is a predefined set of characters and their corresponding pixel representations.
"""

def add_text_to_matrix(matrix, text, font, position):
    x, y = position
    for char in text:
        if char in font:
            char_pixels = font[char]
            for i in range(len(char_pixels)):
                for j in range(len(char_pixels[i])):
                    if x + j < 32 and y + i < 32:  
                        matrix[y + i][x + j] = char_pixels[i][j]
            x += len(char_pixels[0]) + 1  
    return matrix