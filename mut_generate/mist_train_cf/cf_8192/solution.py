"""
QUESTION:
Create a `draw_triangle` function that takes three parameters: `height`, `symbol`, and `inverted`. The function should draw an inverted triangle with the given height, using the specified symbol, and with the specified orientation. The number of symbols in each row should be equal to the row number multiplied by 2. The function should also return the total number of symbols in the triangle.

The function should validate its inputs, ensuring that `height` is a positive integer, `symbol` is either '*' or '#', and `inverted` is a boolean value. If any input is invalid, the function should print an error message and return. Additionally, if the height is too large to fit on the screen, the function should display a partial triangle with a warning message.
"""

def draw_triangle(height, symbol, inverted):
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        return
    
    if symbol not in ['*', '#']:
        print("Error: Symbol must be either '*' or '#'.")
        return
    
    if inverted not in [True, False]:
        print("Error: Orientation must be either 'True' or 'False'.")
        return
    
    max_width = 2 * height
    if max_width > 50:
        print("Warning: Height is too large to fit on the screen. Displaying a partial triangle.")
        max_width = 50
    
    total_stars = 0
    for i in range(height):
        row_width = (i + 1) * 2
        if row_width > max_width:
            row_width = max_width
        
        total_stars += row_width
        row = symbol * row_width
        
        if inverted:
            print(row.center(max_width))
        else:
            print(row)
    
    print("Total number of stars:", total_stars)