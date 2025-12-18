"""
QUESTION:
Develop a function called `polite_numbers` that takes one parameter `n`. This function should return the nth polite number and the sum of the first nth polite numbers. A polite number is a positive integer that can be written as the sum of two or more consecutive positive integers. Ensure the function can handle large inputs efficiently with a time complexity better than O(n log n). The function should also handle invalid inputs, specifically non-positive integers.
"""

def polite_numbers(n):
    """
    Returns the nth polite number and the sum of the first nth polite numbers.
    
    A polite number is a positive integer that can be written as the sum of two or more consecutive positive integers.

    Args:
        n (int): The position of the polite number to find.

    Returns:
        tuple: A tuple containing the nth polite number and the sum of the first nth polite numbers.
    """
    if n < 1:
        return "Error: input should be a positive integer"
    nth_polite_number = 0
    polite_number_sum = 0
    nth_polite_count = 0
    i = 1
    while nth_polite_count < n:
        if i & (i-1):
            nth_polite_number = i
            polite_number_sum += nth_polite_number
            nth_polite_count += 1
        i += 1
    return nth_polite_number, polite_number_sum