"""
QUESTION:
Create a function called `linear_search` that takes in a list of integers and a target integer. The function should return the index of the target if found in the list, and -1 otherwise. Implement the function using a linear search algorithm, which iterates over the list one element at a time, checking for a match with the target.
"""

def linear_search(arr, target):
    """
    Implement linear search on a list.
    Parameters:
        arr(list): A list of integers.
        target(int): An integer to be searched.
    Returns:
        index of target if found, -1 otherwise.
    """

    # Step 1.  Iterate over the list one by one
    for i in range(len(arr)):

        # Step 2. Check if current element is equal to the target.
        if arr[i] == target:

            # Step 3. If the current element is equal to the target, return its index.
            return i

    # Step 4. If the code reaches here, it means the target is not in the list. Return -1.
    return -1