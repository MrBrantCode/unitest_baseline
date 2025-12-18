"""
QUESTION:
Write a function named print_spiral that takes a 2D array as input and prints its elements in a clockwise spiral order. The function should be able to handle arrays with uneven lengths and empty arrays without crashing or producing unexpected results. The array can have a maximum size of 1000 elements. The input array can contain negative integers and decimal numbers.
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