"""
QUESTION:
Create a function `calculate_average` that takes a 2D array as input and returns the row number (0-indexed) and the corresponding average value. The array is filled with unique random numbers. The average of each row should be rounded to 2 decimal places. Implement the average calculation algorithm without using any built-in functions or libraries to calculate the average. The function should be optimized for efficiency.
"""

def calculate_average(array):
    """
    This function calculates the row number (0-indexed) and the corresponding average value 
    of the 2D array. The average of each row is rounded to 2 decimal places.
    
    Args:
    array (list): A 2D list of unique random numbers.
    
    Returns:
    tuple: A tuple containing the row number and the corresponding average value.
    """
    highest_average = 0
    highest_row = 0

    for row in range(len(array)):
        row_sum = 0
        for column in range(len(array[row])):
            row_sum += array[row][column]

        row_average = round(row_sum / len(array[row]), 2)
        if row_average > highest_average:
            highest_average = row_average
            highest_row = row

    return highest_row, highest_average