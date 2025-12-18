"""
QUESTION:
Create a function `calculate_average` that takes a 2D array as input and returns the row number with the highest average value along with its corresponding average value. The 2D array will be filled with unique random numbers. The average of each row should be rounded to 5 decimal places. Implement the average calculation algorithm yourself without using any built-in functions or libraries. Note that the input array will have 1000 rows and 1000 columns.
"""

def calculate_average(array):
    highest_average = 0
    highest_row = 0
    
    for i in range(len(array)):
        row_sum = 0
        for j in range(len(array[i])):
            row_sum += array[i][j]
        
        average = row_sum / len(array[i])
        
        if average > highest_average:
            highest_average = average
            highest_row = i
    
    return highest_row, round(highest_average, 5)