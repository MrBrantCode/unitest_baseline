"""
QUESTION:
Write a function `weighted_median_occurrences(arr, weights)` that takes a list of positive integers `arr` and a corresponding list of weights `weights` as input. The function should return the integer that occurs at the weighted median frequency. If multiple numbers share identical frequency, resolve the tie using the total weight for each number. The number with greater total weight will be selected. In a tie on total weight, return the lower number. If no weighted median is found due to even number of frequency classes or if the lists are unequal in length, return -1.
"""

def weighted_median_occurrences(arr, weights):
    if len(arr) != len(weights):
        return -1

    frequency = {}
    weights_dict = {}

    for i in range(len(arr)):
        frequency[arr[i]] = frequency.get(arr[i], 0) + 1
        weights_dict[arr[i]] = weights_dict.get(arr[i], 0) + weights[i]

    frequency_classes = list(frequency.values())
    frequency_classes.sort()

    if len(frequency_classes) % 2 == 0:
        return -1

    median_frequency = frequency_classes[len(frequency_classes) // 2]

    numbers_at_median_frequency = [num for num in frequency if frequency[num] == median_frequency]

    if len(numbers_at_median_frequency) == 1:
        return numbers_at_median_frequency[0]
    else:
        weights_at_median_frequency = [(num, weights_dict[num]) for num in numbers_at_median_frequency]
        weights_at_median_frequency.sort(key=lambda x: (-x[1], x[0]))
        return weights_at_median_frequency[0][0]