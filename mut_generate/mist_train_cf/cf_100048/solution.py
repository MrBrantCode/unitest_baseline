"""
QUESTION:
Design a function `perfect_squares(sequence)` that takes a list of integers `sequence` and returns a new list containing all the numbers that are perfect squares. The function should also print the total number of perfect squares found and the percentage of perfect squares in the original list. If the input list is empty or contains no perfect squares, the function should return an empty list and print an appropriate message.
"""

import math
def find_perfect_squares(sequence):
    squares = []
    count = 0
    
    for i in sequence:
        if math.sqrt(i) == int(math.sqrt(i)):
            squares.append(i)
            count += 1
            
    if len(sequence) == 0:
        print("The input list is empty.")
    elif count == 0:
        print("No perfect squares found in the input list.")
    else:
        print("Total number of perfect squares found: ", count)
        print("Percentage of perfect squares in the original list: ", count/len(sequence)*100)
        
    return squares