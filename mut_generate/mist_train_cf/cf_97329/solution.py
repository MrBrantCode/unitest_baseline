"""
QUESTION:
Create a function named `sum_after_removal` that takes a list of integers `array` and an integer `index` as input. Remove the element at the specified `index` from the `array`, calculate the sum of the remaining elements, and apply the following rules: 
- If the removed element is greater than 10, multiply the sum by 2.
- If the removed element is between 5 and 10 (inclusive), subtract 1 from each element in the array before calculating the sum.
- If the removed element is less than 5, add the index of each element in the array to the sum. 
Finally, return the modified sum.
"""

def sum_after_removal(array, index):
    """
    Remove the element at the specified index from the array, 
    calculate the sum of the remaining elements, and apply 
    the given rules.

    Args:
    array (list): A list of integers.
    index (int): The index of the element to be removed.

    Returns:
    int: The modified sum of the remaining elements.
    """

    # Remove the element at the specified index
    removed_element = array.pop(index)

    # Calculate sum of remaining elements in the array
    sum_of_elements = sum(array)

    # Check conditions based on the removed element
    if removed_element > 10:
        sum_of_elements *= 2
    elif 5 <= removed_element <= 10:
        sum_of_elements = sum(element - 1 for element in array)
    else:
        sum_of_elements += sum(range(len(array)))

    return sum_of_elements