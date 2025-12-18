"""
QUESTION:
Write a function `averages_descending` that takes a nested list of integers as input. The function should calculate the average of each sublist, treating empty sublists as having an average of 0, and return a list of these averages in descending order.
"""

def averages_descending(arr):
    averages = []
    for sublist in arr:
        if sublist:
            avg = sum(sublist) / len(sublist)
            averages.append(avg)
        else:
            averages.append(0)
    return sorted(averages, reverse=True)