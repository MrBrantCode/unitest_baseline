"""
QUESTION:
Create a function `calculate_statistics` that takes a list of numbers as input and returns a tuple containing the mean, mode(s), median, and standard deviation. 

The function should have a time complexity of O(n) and should not use any built-in statistical libraries or functions. The function should handle both odd and even lengths of input lists when calculating the median, and should return all modes if there are multiple numbers with the highest count.
"""

def calculate_statistics(numbers):
    # Initialize variables to calculate mean
    total_sum = 0
    count = 0
    
    # Initialize dictionary to store count of each number
    num_count = {}

    # Iterate through each number
    for num in numbers:
        # Update sum and count
        total_sum += num
        count += 1
        
        # Update count of each number
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    # Calculate mean
    mean = total_sum / count

    # Calculate mode(s)
    max_count = max(num_count.values())
    mode = [num for num, freq in num_count.items() if freq == max_count]

    # Calculate median
    sorted_numbers = sorted(numbers)
    if count % 2 == 1:
        median = sorted_numbers[count // 2]
    else:
        mid1 = sorted_numbers[count // 2 - 1]
        mid2 = sorted_numbers[count // 2]
        median = (mid1 + mid2) / 2

    # Calculate standard deviation
    sum_squared_diff = 0
    for num in numbers:
        squared_diff = (num - mean) ** 2
        sum_squared_diff += squared_diff
    variance = sum_squared_diff / count
    std_dev = variance ** 0.5

    return mean, mode, median, std_dev