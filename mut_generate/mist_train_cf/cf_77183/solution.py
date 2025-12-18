"""
QUESTION:
Write a function `median(l: list)` that calculates the median of elements in a list without using sorting techniques or built-in functions. The function should handle cases with even or odd numbers of elements, duplicates, negative values, and large numbers.
"""

def median(l: list):
    hist = {}
    for num in l:
        hist[num] = hist.get(num, 0) + 1

    counts = total = 0
    for num in sorted(hist.keys()):
        counts += hist[num]
        if counts >= len(l)/2:
            if len(l) % 2 == 1 or counts > len(l)/2:
                return num
            else:
                for next_num in sorted(hist.keys()):
                    if next_num > num:
                        return (num + next_num) / 2