"""
QUESTION:
Write a function `top_10_most_frequent` that takes a list of integers as input and returns a list of the top 10 most frequent integers and their respective frequencies. The output list should be sorted in descending order based on the frequencies. If two integers have the same frequency, they should be sorted in ascending order. If there are less than 10 integers in the input list, return all of them.
"""

def top_10_most_frequent(nums):
    # Create a dictionary to store the frequency of each integer
    freq_dict = {}

    # Count the frequency of each integer
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # Sort the dictionary based on frequencies in descending order and integers in ascending order
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))

    # Return the top 10 most frequent integers
    return sorted_freq[:10]