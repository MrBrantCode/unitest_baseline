"""
QUESTION:
Write a function `hex_to_dec` that takes a 2D matrix of hexadecimal strings as input, converts each element from hexadecimal to decimal, and returns the modified matrix along with the total sum of all decimal values. The function should handle invalid hexadecimal values by returning an error message instead of the expected output.
"""

def hex_to_dec(matrix_data):
    """
    Converts a 2D matrix of hexadecimal strings to decimal, 
    and returns the modified matrix along with the total sum of all decimal values.

    Args:
        matrix_data (list): A 2D matrix of hexadecimal strings.

    Returns:
        tuple: A tuple containing the modified matrix and the total sum of decimal values.
        str: An error message if invalid hexadecimal value is found.
    """
    total_sum = 0
    try:
        for i in range(len(matrix_data)):
            for j in range(len(matrix_data[i])):
                dec_val = int(matrix_data[i][j], 16) 
                matrix_data[i][j] = dec_val 
                total_sum += dec_val 
        return matrix_data, total_sum 
    except ValueError:   
        return "Invalid hexadecimal value found in the matrix."