"""
QUESTION:
Design a function `find_median(arrays)` to calculate the median of multiple given arrays of non-negative integers with varying lengths without sorting. The function should accommodate for both odd and even numbers of elements as well as any potential duplicates within the arrays.
"""

def find_median(arrays):
    count = 0
    histogram = {}

    for array in arrays:
        for num in array:
            if num not in histogram:
                histogram[num] = 0
            histogram[num] += 1
            count += 1

    middle = count // 2

    cumsum = 0
    for num in range(max(histogram)+1):
        if num in histogram:
            cumsum += histogram[num]
            if cumsum > middle:
                if count % 2 == 1 or cumsum - histogram[num] < middle:
                    return num
                for next_num in range(num+1, max(histogram)+1):
                    if next_num in histogram:
                        return (num + next_num) / 2