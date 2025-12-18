"""
QUESTION:
Create a function `create_dict_from_list` that takes a list of integers as input and returns a dictionary where each key represents a unique even number from the list and each value represents the cumulative product of its 1-indexed positions. The function should only consider even numbers from the input list and ignore odd numbers.
"""

def create_dict_from_list(given_list):
    even_dict = {}
    pos_dict = {}

    for i, num in enumerate(given_list):
        if num % 2 == 0:  # check if number is even
            if num not in pos_dict:  # if number is not yet in pos_dict, add it
                pos_dict[num] = i + 1  #Positions are 1-indexn based
                even_dict[num] = 1  #initialize cumulated product to 1
            else:  # if number is already in pos_dict, update position and product in even_dict
                even_dict[num] *= (i + 1) / pos_dict[num]
                pos_dict[num] = i + 1

    return even_dict