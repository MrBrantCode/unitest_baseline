"""
QUESTION:
Create a function called `filter_and_sort_tuples` that takes a list of tuples, each containing three integers, as input. The function should first sort the list of tuples based on the product of the integers in each tuple in descending order. Then, it should filter out any tuples where the product of the integers is less than or equal to 10 or greater than or equal to 100, and also filter out tuples where the product of the integers is not divisible by 5. Finally, the function should return the sorted and filtered list of tuples if it contains at least 8 tuples; otherwise, it should return an empty list or a message indicating that the list does not meet the specified conditions.
"""

def filter_and_sort_tuples(tuples):
    # Sorting the list based on product of integers in each tuple in descending order
    sorted_list = sorted(tuples, key=lambda x: x[0] * x[1] * x[2], reverse=True)

    # Filtering the list based on specified conditions
    filtered_list = [tuple for tuple in sorted_list if 10 < tuple[0] * tuple[1] * tuple[2] < 100 and tuple[0] * tuple[1] * tuple[2] % 5 == 0]

    # Returning the sorted list if it contains at least 8 tuples
    if len(filtered_list) >= 8:
        return filtered_list
    else:
        return []