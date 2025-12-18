"""
QUESTION:
Write a function `count_elements` that takes a list of elements as input and returns a list of tuples. Each tuple contains a unique element from the list and its count. The output list should be sorted in descending order of the count. The function should not use any built-in counting functions or methods and should have a time complexity of O(n^2) or better. The input list can contain integers, floats, or strings.
"""

def count_elements(my_list):
    """
    Returns a list of tuples containing unique elements from the input list and their counts.
    The output list is sorted in descending order of the count.

    Time complexity: O(n^2)

    Args:
        my_list (list): A list of elements (int, float, str)

    Returns:
        list: A list of tuples containing unique elements and their counts
    """
    count_list = []
    for element in my_list:
        count = 0
        for item in my_list:
            if element == item:
                count += 1
        if (element, count) not in count_list:
            count_list.append((element, count))
    count_list.sort(key=lambda x: x[1], reverse=True)
    return count_list