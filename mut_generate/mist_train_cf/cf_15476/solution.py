"""
QUESTION:
Write a function max_subset(arr, K) that returns a subset of size K from the given array arr such that the sum of all elements in the subset is the maximum possible value and the difference between the maximum and minimum element in the subset is greater than or equal to 5. The array elements are all positive integers. Return an empty array if no such subset exists.
"""

def max_subset(arr, K):
    """
    Returns a subset of size K from the given array arr such that the sum of all elements in the subset is the maximum possible value 
    and the difference between the maximum and minimum element in the subset is greater than or equal to 5.
    
    Args:
        arr (list): A list of positive integers.
        K (int): The size of the subset.
    
    Returns:
        list: A subset of size K with the maximum sum and a difference of at least 5 between the maximum and minimum elements.
              Returns an empty array if no such subset exists.
    """
    # Check if K is less than or equal to 5
    if K <= 5:
        return []

    # Sort the given array in non-decreasing order
    arr.sort()

    # Create a new array maxSubset of size K and initialize it with the first K elements of arr
    maxSubset = arr[:K]
    # Initialize two variables, maxSum and minDiff, with the sum of maxSubset and the difference between the last and first elements of maxSubset
    maxSum = sum(maxSubset)
    minDiff = maxSubset[-1] - maxSubset[0]

    # Iterate over the remaining elements of arr starting from index K
    for i in range(K, len(arr)):
        # Check if adding arr[i] to maxSubset will violate the difference condition
        if arr[i] - maxSubset[0] < 5:
            continue

        # Check if adding arr[i] to maxSubset will increase the sum
        if arr[i] + maxSum - maxSubset[0] <= maxSum:
            continue

        # Update maxSubset, maxSum, and minDiff
        maxSubset = maxSubset[1:] + [arr[i]]
        maxSum = sum(maxSubset)
        minDiff = maxSubset[-1] - maxSubset[0]

    # Check if a valid subset was found
    if minDiff < 5:
        return []

    return maxSubset