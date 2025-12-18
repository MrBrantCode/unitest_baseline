"""
QUESTION:
Create a function `manageWindows` that takes two parameters: a 2D grid representing the screen dimensions and a list of windows. Each window is defined by its top-left corner coordinates (row, column) and its dimensions (height, width). 

The function should return three values: the total area of the screen covered by windows, the coordinates of any overlapping areas, and the total area of the screen available for placing new windows. 

Assume the screen dimensions and window coordinates are valid, and all windows are placed entirely within the screen boundaries.
"""

def manageWindows(screen, windows):
    total_area_covered = 0
    overlapping_areas = []
    
    for window in windows:
        row, col, height, width = window
        for i in range(row, row + height):
            for j in range(col, col + width):
                if screen[i][j] == 1:
                    overlapping_areas.append((row, col, height, width))
                screen[i][j] = 1
                total_area_covered += 1
    
    available_area = sum(row.count(0) for row in screen)
    
    return total_area_covered, overlapping_areas, available_area