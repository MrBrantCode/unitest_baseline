"""
QUESTION:
Create a function named `generate_pattern(size, color)` that generates a symmetrical, bowtie-shaped pattern of alternating black and white squares. The pattern's size is determined by the `size` parameter, which must be between 3 and 10 (inclusive). The `color` parameter determines the color of the top section of the pattern, with the bottom section being the opposite color. The function should print the pattern as a grid of colors.
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
                    
    for row in pattern:
        print(" ".join(row))