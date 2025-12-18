"""
QUESTION:
Create a function `frequency_count` that takes an array of numbers as input and returns a dictionary containing the frequency of each number, the numbers with the highest frequency, and the numbers with the lowest frequency. The function must run in O(n) time complexity, where n is the length of the input array.
"""

def frequency_count(arr):
    frequency = {}
    max_frequency = 0
    min_frequency = float('inf')

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        max_frequency = max(max_frequency, frequency[num])
        min_frequency = min(min_frequency, frequency[num])

    most_frequent = [num for num, freq in frequency.items() if freq == max_frequency]
    least_frequent = [num for num, freq in frequency.items() if freq == min_frequency]

    return {
        "frequency": frequency,
        "most_frequent": most_frequent,
        "least_frequent": least_frequent
    }