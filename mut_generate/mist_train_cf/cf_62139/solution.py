"""
QUESTION:
Implement the function `insertion_sort(arr)` that sorts the input array in ascending order and returns a tuple containing the sorted array and the total number of moves (swaps and shifts) made during the sorting process. The input array can have up to 10^5 elements.
"""

def insertion_sort(arr):
    """
    Sorts the input array in ascending order and returns a tuple containing 
    the sorted array and the total number of moves (swaps and shifts) made 
    during the sorting process.

    Args:
    arr (list): The input array to be sorted.

    Returns:
    tuple: A tuple containing the sorted array and the total number of moves.
    """
    moves = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            moves+=1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr, moves