"""
QUESTION:
Create a function `sort_and_evaluate` that takes a list of tuples as input, where each tuple contains a name (string), age (integer), and number of siblings (integer). The function should sort the list in ascending order by age, then in descending order by number of siblings, and finally lexicographically by name. It should return the sorted list, the average age, and the total number of siblings.
"""

def sort_and_evaluate(tuples):
    """
    Sorts the list of tuples by age in ascending order, then by number of siblings in descending order, 
    and finally by name lexicographically. Returns the sorted list, the average age, and the total number of siblings.

    Args:
        tuples (list): A list of tuples containing a name (string), age (integer), and number of siblings (integer).

    Returns:
        tuple: A tuple containing the sorted list, the average age, and the total number of siblings.
    """

    # sorting the list of tuples
    sorted_tuples = sorted(tuples, key=lambda x: (x[1], -x[2], x[0]))

    # calculating the average age and the total number of siblings
    sum_age = sum([i[1] for i in sorted_tuples])
    total_siblings = sum([i[2] for i in sorted_tuples])
    average_age = sum_age / len(sorted_tuples)

    # returning the results
    return sorted_tuples, average_age, total_siblings