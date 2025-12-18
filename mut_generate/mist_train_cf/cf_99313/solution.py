"""
QUESTION:
Create a function `generate_pattern(size, color)` that generates a grid pattern based on the given size and color. The function should take two parameters: `size` (an integer between 3 and 10) and `color` (either "black" or "white"). The pattern should be a symmetrical grid of squares, with the top and bottom sections inverted from each other, and no two adjacent squares having the same color.
"""

def generate_pattern(size, color):
    if size < 3 or size > 10:
        print("Invalid size. Please enter a size between 3 and 10.")
        return
    
    if color.lower() == "black":
        colors = ["black", "white"]
    elif color.lower() == "white":
        colors = ["white", "black"]
    else:
        print("Invalid color. Please enter either black or white.")
        return
    
    pattern = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(colors[0])
            else:
                row.append(colors[1])
        pattern.append(row)
        
    for i in range(size):
        for j in range(size):
            if i < size // 2:
                if j < i or j >= size - i:
                    pattern[i][j], pattern[size - i - 1][j] = pattern[size - i - 1][j], pattern[i][j]
            elif i > size // 2:
                if j < size - i - 1 or j >= i:
                    pattern[i][j], pattern[size - i - 1][j] = pattern[size - i - 1][j], pattern[i][j]
                    
    return pattern