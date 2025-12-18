"""
QUESTION:
Implement a function called `strange_sort_vector` that takes a vector of integers as input and returns two vectors. The first vector contains the input integers sorted in a peculiar order, starting with the minimum value, then the maximum of the remaining integers, then the minimum, and so on. The second vector contains the sum of the smallest and the largest numbers in the list in each step of this peculiar sorting. The function should handle the case where the input vector is empty.
"""

def strange_sort_vector(vec):
    """
    This function takes a vector of integers as input and returns two vectors.
    The first vector contains the input integers sorted in a peculiar order, 
    starting with the minimum value, then the maximum of the remaining integers, 
    then the minimum, and so on. The second vector contains the sum of the smallest 
    and the largest numbers in the list in each step of this peculiar sorting.

    Args:
        vec (list): A list of integers.

    Returns:
        tuple: A tuple containing two lists. The first list is the sorted vector and 
        the second list is the sum of the smallest and the largest numbers in each step.
    """

    # Sort the input vector
    vec.sort()

    # Initialize two empty lists to hold the sorted values and the sums
    sorted_vec = []
    sums = []

    # Iterate over the sorted vector
    while vec:
        # Get the minimum value and remove it from the vector
        min_val = vec.pop(0)
        sorted_vec.append(min_val)

        # If the vector is not empty after removing the minimum value
        if vec:
            # Get the maximum value and remove it from the vector
            max_val = vec.pop()
            sorted_vec.append(max_val)
            # Calculate the sum of the minimum and maximum values and append it to the sums list
            sums.append(min_val + max_val)
        else:
            # If the vector is empty after removing the minimum value, append the minimum value to the sums list
            sums.append(min_val)

    # Return the sorted vector and the sums list
    return sorted_vec, sums