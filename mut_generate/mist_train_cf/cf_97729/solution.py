"""
QUESTION:
Given a list of integers, design a function `perfect_squares(sequence)` that returns a new list containing all the numbers that are perfect squares in the sequence. The function should also print out the total number of perfect squares found and the percentage of perfect squares in the original list. If the input list is empty or contains no perfect squares, the function should return an empty list and print out an appropriate message.
"""

import math
def perfect_squares(sequence):
    squares = [i for i in sequence if math.sqrt(i) == int(math.sqrt(i))]
    count = len(squares)
    
    if len(sequence) == 0:
        print("The input list is empty.")
    elif count == 0:
        print("No perfect squares found in the input list.")
    else:
        print("Total number of perfect squares found: ", count)
        print("Percentage of perfect squares in the original list: ", count/len(sequence)*100)
        
    return squares