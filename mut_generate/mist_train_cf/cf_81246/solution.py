"""
QUESTION:
Develop a function called `penultimate_in_bounds` that takes two parameters: a list of integers `seq` and a list of two integers `bounds` representing the lower and upper bounds of a range. The function should return the second-highest unique integer in `seq` that falls within the range defined by `bounds`. If there is only one unique integer within the range, or no integers at all, return 'No penultimate element in bounds'.
"""

def penultimate_in_bounds(seq, bounds):
    filtered = [elem for elem in seq if bounds[0] <= elem <= bounds[1]]
    unique_sorted_filtered = sorted(set(filtered), reverse=True)
    if len(unique_sorted_filtered) > 1:
        return unique_sorted_filtered[1]
    else:
        return 'No penultimate element in bounds'