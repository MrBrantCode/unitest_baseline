"""
QUESTION:
Write two functions, `hasPairWithSum` and `hasTripletWithSum`, that take an array of integers and a target sum as input. The `hasPairWithSum` function should return True if there exists a pair of numbers in the array that add up to the target sum, and False otherwise. The `hasTripletWithSum` function should return True if there exists a triplet of numbers in the array that add up to the target sum, and False otherwise. The functions should not modify the input array.
"""

def hasPairWithSum(arr, sum):
    """
    Checks if there exists a pair of numbers in the array that add up to the target sum.

    Args:
    arr (list): A list of integers.
    sum (int): The target sum.

    Returns:
    bool: True if a pair is found, False otherwise.
    """
    complementSet = set()
    for num in arr:
        complement = sum - num
        if complement in complementSet:
            return True
        complementSet.add(num)
    return False

def hasTripletWithSum(arr, sum):
    """
    Checks if there exists a triplet of numbers in the array that add up to the target sum.

    Args:
    arr (list): A list of integers.
    sum (int): The target sum.

    Returns:
    bool: True if a triplet is found, False otherwise.
    """
    for i in range(0, len(arr)-2):
        twoSum = sum - arr[i]
        if hasPairWithSum(arr[i+1:], twoSum):
            return True
    return False