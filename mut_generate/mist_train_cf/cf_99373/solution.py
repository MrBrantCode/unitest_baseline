"""
QUESTION:
Design a function `perfect_squares(sequence)` that takes a list of integers as input. The function should return a new list containing all the numbers that are perfect squares in the input list, print the total number of perfect squares found, and print the percentage of perfect squares in the original list. If the input list is empty or contains no perfect squares, the function should return an empty list and print an appropriate message. The function should be efficient and use minimal memory to handle large input lists.
"""

import math

def find_perfect_squares(sequence):
    perfect_squares_list = [i for i in sequence if math.sqrt(i) == int(math.sqrt(i))]
    
    if not sequence:
        print("The input list is empty.")
    elif not perfect_squares_list:
        print("No perfect squares found in the input list.")
    else:
        print("Total number of perfect squares found: ", len(perfect_squares_list))
        print("Percentage of perfect squares in the original list: ", len(perfect_squares_list)/len(sequence)*100)
        
    return perfect_squares_list