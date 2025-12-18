"""
QUESTION:
Write a function `calculateCellDimensions` that takes four parameters: `itemInSection`, `normalColumnHeight`, `featuredColumnWidth`, and `featuredColumnHeight`. The function should return a tuple `(cellWidth, cellHeight)` representing the width and height of a cell in a grid based on its position in the section. If the item's position in the section (0-indexed) plus 1 is divisible by 7 and is not equal to 0, set `cellWidth` to `featuredColumnWidth` and `cellHeight` to `featuredColumnHeight`. Otherwise, set `cellHeight` to `normalColumnHeight` and `cellWidth` to `normalColumnHeight` by default.
"""

def calculateCellDimensions(itemInSection, normalColumnHeight, featuredColumnWidth, featuredColumnHeight):
    cellWidth = normalColumnHeight
    cellHeight = normalColumnHeight
    
    if (itemInSection + 1) % 7 == 0 and itemInSection != 0:
        cellWidth = featuredColumnWidth
        cellHeight = featuredColumnHeight
    
    return (cellWidth, cellHeight)