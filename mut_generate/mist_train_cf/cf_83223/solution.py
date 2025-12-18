"""
QUESTION:
Write a function named `corrected_trimmed_mean` that takes a list `l` and a float `trim_percentage` as input. The function should calculate the trimmed mean of the list without sorting it or using any external library functions. The list `l` can contain tuples with negative integers and complex numbers. The function should trim the list by removing a percentage of extreme values from both ends of the distribution and then compute the average of the remaining numbers. The percentage of extreme values to be removed is specified by `trim_percentage`.
"""

def corrected_trimmed_mean(l: list, trim_percentage: float):
    trim_amount = int(len(l) * trim_percentage)
    for i in range(trim_amount):
        min_value = min(l, key=lambda x: abs(x.real if isinstance(x, complex) else x))
        max_value = max(l, key=lambda x: abs(x.real if isinstance(x, complex) else x))
        l.remove(min_value)
        l.remove(max_value)

    return sum(l)/len(l)