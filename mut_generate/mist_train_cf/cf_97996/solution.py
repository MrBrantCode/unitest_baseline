"""
QUESTION:
Write a function named `sum_even_numbers` that takes an array of 10 integers as input, where the first 5 elements are even numbers and the next 5 elements are odd numbers. The function should sum the even numbers from the first 5 elements and return the sum if it is greater than 10 and less than 20. The function should also count the total number of even and odd elements in the array and print them. Do not use built-in sum() function.
"""

def sum_even_numbers(arr):
    """
    This function takes an array of 10 integers as input, sums the even numbers 
    from the first 5 elements if the sum is greater than 10 and less than 20, 
    and prints the total number of even and odd elements in the array.

    Parameters:
    arr (list): A list of 10 integers.

    Returns:
    int: The sum of even numbers if it is within the specified range, otherwise None.
    """
    even_count = 0
    odd_count = 0
    even_sum = 0
    for i in range(len(arr)):
        if i < 5 and arr[i] % 2 == 0:
            even_sum += arr[i]
            even_count += 1
        elif arr[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even elements:", even_count)
    print("Odd elements:", odd_count)
    if even_sum > 10 and even_sum < 20:
        return even_sum