"""
QUESTION:
Create a function called `rearrange_three_elements` that takes an array of integers as input. The function should return `True` if it is possible to rearrange the array by swapping at most 3 pairs of adjacent elements such that the sum of all elements smaller than the first element is a prime number and the count of such elements is odd, and `False` otherwise.
"""

def rearrange_three_elements(arr):
    # Handle the edge case
    if len(arr) == 0:
        return True

    def check_prime(n):
        # Handle the edge case
        if n < 2: 
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Step 1: Original bubble sort
    n = len(arr)
    swap_cnt = 0
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_cnt += 1
                if swap_cnt > 3:
                    return False
    
    # Step 2: Count the number of smaller elements
    num_of_smaller = sum(1 for x in arr if x < arr[0])
    
    # Step 3: Check conditions
    total_sum = sum(x for x in arr if x < arr[0])
    return num_of_smaller % 2 == 1 and check_prime(total_sum)