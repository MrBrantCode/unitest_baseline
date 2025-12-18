"""
QUESTION:
Write a function `find_mode_and_median` that takes a list of integers as input and returns a tuple of two values: the mode and the median of the numbers in the list that are multiples of 3 and less than 100. The mode should be unique and in case of multiple modes, choose the one with the highest frequency. If there are no numbers that satisfy the criteria, return None for both the mode and median.
"""

def find_mode_and_median(numbers):
    # Create an empty dictionary to store the frequency of each number
    frequency = {}
    
    # Iterate through the list of integers and check if each number satisfies the criteria
    for num in numbers:
        if num % 3 == 0 and num < 100:
            # Update the frequency of each number that satisfies the criteria
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
    
    # Find the mode by iterating through the dictionary and finding the number with the highest frequency
    mode = None
    max_frequency = 0
    for num, freq in frequency.items():
        if freq > max_frequency:
            mode = num
            max_frequency = freq
        elif freq == max_frequency:
            if num < mode:
                mode = num
    
    # Return None for the mode if the dictionary is empty or there are no numbers that satisfy the criteria
    if len(frequency) == 0 or mode is None:
        mode = None
    
    # Create a new list containing only the numbers that satisfy the criteria and sort it in ascending order
    multiples_of_3 = [num for num in numbers if num % 3 == 0 and num < 100]
    multiples_of_3.sort()
    
    # Return None for the median if the list is empty
    if len(multiples_of_3) == 0:
        median = None
    else:
        # Calculate the median based on the length of the list
        if len(multiples_of_3) % 2 == 1:
            median = multiples_of_3[len(multiples_of_3) // 2]
        else:
            mid = len(multiples_of_3) // 2
            median = (multiples_of_3[mid - 1] + multiples_of_3[mid]) / 2
    
    return mode, median