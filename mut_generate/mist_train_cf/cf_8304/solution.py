"""
QUESTION:
Create a function `is_divisible_by_5` that takes a list of integers as input. The function should return True if the sum of the absolute values of the unique numbers in the list is divisible by 5 and the length of the list is greater than or equal to 10. Otherwise, it should return False. The function should not use any built-in Python functions or libraries, and it should achieve a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

def is_divisible_by_5(numbers):
    # Count the occurrences of each number in the list
    number_count = {}
    for num in numbers:
        number_count[num] = number_count.get(num, 0) + 1
    
    # Calculate the sum of the absolute values of the unique numbers
    total_sum = sum(abs(num) for num in number_count)
    
    # Check if the sum is divisible by 5 and the length of the list is >= 10
    return total_sum % 5 == 0 and len(numbers) >= 10