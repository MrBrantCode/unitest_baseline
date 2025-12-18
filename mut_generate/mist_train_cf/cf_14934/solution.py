"""
QUESTION:
Write a function `modulo_sum` that calculates the sum of all elements in an integer array after applying a modulo operation to each element. The function should take two parameters: `arr`, an integer array of size n (1 <= n <= 10^5) with elements in the range 0 <= arr[i] <= 10^5, and `m`, an integer in the range 1 <= m <= 10^9. The function should return an integer representing the sum of the resulting values after the modulo operation. The solution should have a time complexity of O(n) and space complexity of O(1).
"""

def modulo_sum(arr, m):
    """
    Calculates the sum of all elements in an integer array after applying a modulo operation to each element.

    Args:
        arr (list): An integer array of size n (1 <= n <= 10^5) with elements in the range 0 <= arr[i] <= 10^5.
        m (int): An integer in the range 1 <= m <= 10^9.

    Returns:
        int: The sum of the resulting values after the modulo operation.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    # Initialize a variable total_sum to 0 to keep track of the sum of the resulting values.
    total_sum = 0
    
    # Iterate over each element num in the array arr.
    for num in arr:
        # Apply the modulo operation num % m to the element num.
        # Add the resulting value to the total_sum.
        total_sum += num % m
    
    # Return the total_sum.
    return total_sum