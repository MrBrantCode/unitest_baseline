"""
QUESTION:
Implement the function `is_arithmetic(nums: List[int]) -> bool` to determine if the given list of numbers is an arithmetic sequence. The list should have at least three numbers, the second number should be a prime number, and the first and last numbers should be divisible by the common difference. Return `True` if the list is an arithmetic sequence, `False` otherwise. The list will contain only integers and have a length between 1 and 10^5.
"""

def is_arithmetic(nums):
    """
    This function determines if the given list of numbers is an arithmetic sequence.
    
    Parameters:
    nums (List[int]): A list of integers.
    
    Returns:
    bool: True if the list is an arithmetic sequence, False otherwise.
    """
    
    # Check if the length of the list is less than 3
    if len(nums) < 3:
        return False
    
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Check if the second number is a prime number
    if not is_prime(nums[1]):
        return False
    
    # Calculate the common difference
    common_diff = nums[1] - nums[0]
    
    # Check if the difference between each pair of consecutive terms is equal to the common difference
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] != common_diff:
            return False
    
    # Check if the first and last numbers are divisible by the common difference
    if nums[0] % common_diff != 0 or nums[-1] % common_diff != 0:
        return False
    
    return True