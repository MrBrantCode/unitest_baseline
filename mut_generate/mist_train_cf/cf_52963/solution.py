"""
QUESTION:
Write a function named `cumulative_sum` that calculates the cumulative sum of all numerical values (integers and floats) in a given list of tuples. The function should iterate over each tuple in the list and each element in the tuple, adding up the numerical values regardless of their position. The function should return the cumulative sum.
"""

def cumulative_sum(tuples_list):
    cum_sum = 0
    for tup in tuples_list:
        for elem in tup:
            if type(elem) in (int, float):
                cum_sum += elem
    return cum_sum