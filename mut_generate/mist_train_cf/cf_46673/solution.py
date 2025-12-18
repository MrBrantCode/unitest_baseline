"""
QUESTION:
Write a Python function named `sort_tuples` that takes a list of integer tuples as input, where each tuple contains a value and a weight. The function should sort the list of tuples in descending order based on the product of the value and the weight of each tuple. In case of a tie, sort the tuples by their weights in descending order. The function must implement the sorting algorithm without using any built-in sort functions.
"""

def sort_tuples(list_of_tuples):
    """
    Sorts a list of integer tuples in descending order based on the product of the value and the weight of each tuple.
    In case of a tie, sorts the tuples by their weights in descending order.

    Args:
        list_of_tuples (list): A list of integer tuples, where each tuple contains a value and a weight.

    Returns:
        list: The sorted list of tuples.
    """

    # Bubble sort algorithm
    n = len(list_of_tuples)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Multiply value and weight, compare the product.
            if list_of_tuples[j][0] * list_of_tuples[j][1] < list_of_tuples[j+1][0] * list_of_tuples[j+1][1]:
                list_of_tuples[j], list_of_tuples[j+1] = list_of_tuples[j+1], list_of_tuples[j]
            elif list_of_tuples[j][0] * list_of_tuples[j][1] == list_of_tuples[j+1][0] * list_of_tuples[j+1][1]:
                # If the product is equal, compare the weights.
                if list_of_tuples[j][1] < list_of_tuples[j+1][1]:
                    list_of_tuples[j], list_of_tuples[j+1] = list_of_tuples[j+1], list_of_tuples[j]
    return list_of_tuples