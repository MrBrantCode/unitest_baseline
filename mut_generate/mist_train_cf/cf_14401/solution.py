"""
QUESTION:
Design a function named `find_median_age` that takes a list of integers representing classmates' ages and returns the median age as a float. If the number of ages is even, the function should return the average of the two middle ages. If the number of ages is odd, the function should return the middle age.
"""

def find_median_age(ages):
    ages.sort()
    length = len(ages)

    if length % 2 == 0:
        middle1 = length // 2 - 1
        middle2 = length // 2
        return (ages[middle1] + ages[middle2]) / 2
    else:
        middle = length // 2
        return ages[middle]