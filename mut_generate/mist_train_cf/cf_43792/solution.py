"""
QUESTION:
Create a function called "createMatrix" that generates a square matrix of dimension nxn with sequential elements proceeding in a row-major sequence commencing from 1 to n squared. The function should validate the input being passed into it. The input should be an integer between 1 and 10 (inclusive). If the input is not valid, the function should return an error message. The function should also handle cases where the input is an integer in float format (e.g., 4.0).
"""

def createMatrix(n):
    #check if n is a positive integer within the range
    if type(n) != int and not (isinstance(n, float) and n.is_integer()):
        return 'Invalid input. Enter a positive integer between 1 and 10.'
    elif n <= 0 or n > 10:
        return 'Invalid input. Enter a positive integer between 1 and 10.'
    else:
        n = int(n) # if integer came in float format
        matrix = []
        count = 1
        for i in range(n):
            row = []
            for j in range(n):
                row.append(count)
                count += 1
            matrix.append(row)
        return matrix