"""
QUESTION:
Write a function `sort_tuples` that takes a list of tuples as input, where each tuple contains three integers. The function should sort the list based on the product of the integers in each tuple in descending order. It should ignore any tuples where the product of the integers is less than or equal to 10 or greater than or equal to 100. The function should return the sorted list if it contains at least 8 tuples, otherwise return an empty list or a message indicating the list does not meet the conditions.
"""

def sort_tuples(tuples):
    sorted_list = sorted(tuples, key=lambda x: x[0] * x[1] * x[2], reverse=True)
    filtered_list = [tuple for tuple in sorted_list if 10 < tuple[0] * tuple[1] * tuple[2] < 100 and tuple[0] * tuple[1] * tuple[2] % 5 == 0]
    return filtered_list if len(filtered_list) >= 8 else []