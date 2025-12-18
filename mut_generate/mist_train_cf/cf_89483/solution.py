"""
QUESTION:
Write a function `unique_prime_elements` that calculates the total number of unique prime elements in a given 2D array. The input array contains sub-arrays with two elements each, which can be prime numbers (positive or negative) or floating-point numbers. The function should return the total count of unique elements in the array.
"""

def unique_prime_elements(array):
    def is_prime(n):
        """Check if a number is prime."""
        if not isinstance(n, int):
            return False
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    unique_elements = set()
    for sub_array in array:
        for num in sub_array:
            if is_prime(abs(num)):  # Use absolute value to handle negative numbers
                unique_elements.add(num)
    return len(unique_elements)