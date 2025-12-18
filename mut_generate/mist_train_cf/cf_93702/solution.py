"""
QUESTION:
Create a function called `print_spiral(array)` that prints the content of a 2D array in a clockwise spiral order. The array can contain negative integers and decimal numbers, and it can have uneven lengths. The function should handle empty arrays and arrays with a maximum size of 1000 elements without crashing or producing unexpected results. The input array is a 2D list of numbers, and the function does not return any value.
"""

def print_spiral(array):
    if not array or not array[0]:
        return

    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # Traverse top row
        for col in range(startCol, endCol + 1):
            print(array[startRow][col])

        # Traverse right column
        for row in range(startRow + 1, endRow + 1):
            print(array[row][endCol])

        # Traverse bottom row
        if startRow < endRow:
            for col in range(endCol - 1, startCol - 1, -1):
                print(array[endRow][col])

        # Traverse left column
        if startCol < endCol:
            for row in range(endRow - 1, startRow, -1):
                print(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1