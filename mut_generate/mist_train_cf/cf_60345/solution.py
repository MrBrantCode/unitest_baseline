"""
QUESTION:
Create a function `count_equal_numbers(a, b, c)` that takes three integers as input and returns the number of integers that appear more than once and a list of unique integers along with their frequency. The function should handle potential errors and exceptions during execution.
"""

def count_equal_numbers(a, b, c):
    try:
        # Initialize dictionary for each integer and their counts
        dict_nums = {a: 0, b: 0, c: 0}
    
        # Count the frequency of each integer
        for num in [a, b, c]:
            if num in dict_nums:
                dict_nums[num] += 1
            else:
                dict_nums[num] = 1
    
        # Get the numbers that have the same count
        equal_nums = [key for key, value in dict_nums.items() if value > 1]
        count_equal_nums = len(equal_nums)
    
        # Get the unique numbers and their frequency
        unique_nums_with_freq = [(key, value) for key, value in dict_nums.items() if value == 1]
    
        return count_equal_nums, unique_nums_with_freq
    except Exception as e:
        print("An error occurred: ", e)