"""
QUESTION:
Create a recursive function `recursive_sum` that takes a list of integers and a prime number as input, and returns a tuple containing the sum of the elements in the list that are divisible by the prime number and are greater than or equal to 100, along with the count of such elements. The function should only consider the specified conditions while calculating the sum and count.
"""

def recursive_sum(lst, prime_number, count=0, total_sum=0):
    """
    This function recursively calculates the sum of elements in a list that are divisible by a prime number and are greater than or equal to 100.
    
    Args:
        lst (list): A list of integers.
        prime_number (int): A prime number.
        count (int, optional): The count of elements that meet the specified conditions. Defaults to 0.
        total_sum (int, optional): The sum of elements that meet the specified conditions. Defaults to 0.

    Returns:
        tuple: A tuple containing the sum of the elements and their count.
    """
    if not lst:
        return total_sum, count
    elif lst[0] % prime_number == 0 and lst[0] >= 100:
        return recursive_sum(lst[1:], prime_number, count+1, total_sum + lst[0])
    else:
        return recursive_sum(lst[1:], prime_number, count, total_sum)