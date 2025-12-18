"""
QUESTION:
Create a function `median_and_mode` that takes a list of integers as input and returns a tuple containing the median and mode of the list. The function should not use built-in functions to calculate the median and mode, and it should not sort the input list. The function should be able to handle lists of any length (even or odd) and should be able to handle negative numbers and repeated occurrences. If there is no mode (i.e., all numbers appear only once), the function should return `None` for the mode.
"""

def median_and_mode(l: list):
    # Check if the list is empty
    if not l:
        return None, None

    # Define a dictionary for counting the occurrences of each number
    dic = {}
    for num in l:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    # From the dictionary, get the list of keys (numbers) and values (counts)
    keys = list(dic.keys())
    values = list(dic.values())

    # Compute the median
    total_n = len(l)
    cumulative_n = 0
    median = None
    for i in range(len(keys)):
        cumulative_n += values[i]
        if cumulative_n >= total_n / 2:
            # When the list length is even, the median is the average of the two middle numbers.
            # When it is odd, the median is the middle number.
            if total_n % 2 == 0 and cumulative_n == total_n / 2:
                median = (keys[i] + keys[i + 1]) / 2
            else:
                median = keys[i]
            break

    # Compute the mode
    max_count = max(values)
    mode_index = values.index(max_count)
    mode = keys[mode_index] if max_count > 1 else None

    return median, mode