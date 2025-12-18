"""
QUESTION:
Implement the following functions: `find_mean`, `find_median`, `find_mode`, and `is_sorted`. 

The `find_mean` function should calculate the mean of a given list of numbers. The `find_median` function should calculate the median of a given list of numbers. The `find_median` function should first sort the list of numbers. The `find_mode` function should find the mode of a given list of numbers. The mode is the value that appears most frequently in the list. If there are multiple modes, return all of them in ascending order. The `is_sorted` function should check if a given list of numbers is sorted in ascending order.

The input list can contain both positive and negative integers and can have duplicate values. The solution should handle lists of up to 10^6 numbers and have a time complexity of O(n).
"""

def find_mean(numbers):
    total = len(numbers)
    sum = 0
    
    for num in numbers:
        sum += num
    
    mean = sum / total
    return mean


def find_median(numbers):
    sorted_numbers = sorted(numbers)
    total = len(sorted_numbers)
    
    if total % 2 == 1:  # odd number of elements
        middle_index = total // 2
        median = sorted_numbers[middle_index]
    else:  # even number of elements
        middle_index_1 = total // 2
        middle_index_2 = middle_index_1 - 1
        median = (sorted_numbers[middle_index_1] + sorted_numbers[middle_index_2]) / 2
    
    return median


def find_mode(numbers):
    freq_dict = {}
    
    for num in numbers:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    
    max_freq = max(freq_dict.values())
    modes = [key for key, value in freq_dict.items() if value == max_freq]
    modes.sort()
    
    return modes


def is_sorted(numbers):
    total = len(numbers)
    
    for i in range(total - 1):
        if numbers[i] > numbers[i+1]:
            return False
    
    return True