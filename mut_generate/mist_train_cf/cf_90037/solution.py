"""
QUESTION:
Implement four functions: `find_mean`, `find_median`, `find_mode`, and `is_sorted`, that take a list of integers as input and return the mean, median, mode, and whether the list is sorted in ascending order, respectively. The list can contain both positive and negative integers, and can have duplicate values. The functions should handle lists of up to 10^6 numbers and have a time complexity of O(n).
"""

def calculate_mean(numbers):
    total = len(numbers)
    sum = 0
    
    for num in numbers:
        sum += num
    
    mean = sum / total
    return mean

def calculate_median(numbers):
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

def calculate_mode(numbers):
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

def check_sorted(numbers):
    total = len(numbers)
    
    for i in range(total - 1):
        if numbers[i] > numbers[i+1]:
            return False
    
    return True