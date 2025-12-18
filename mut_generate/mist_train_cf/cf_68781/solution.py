"""
QUESTION:
Write a function `distance_sum_avg_max_min(num_list, num)` that calculates the total distance, average distance, longest distance, and shortest distance between all occurrences of a specific element `num` within a sorted list `num_list`. The function should return these four values if the specific element occurs more than once; otherwise, it returns `None`.
"""

def distance_sum_avg_max_min(num_list, num):
    indices = [i for i, x in enumerate(num_list) if x == num]
    if len(indices) <= 1:
        return None

    distances = [indices[i+1] - indices[i] for i in range(len(indices)-1)]

    total_sum = sum(distances)
    avg = total_sum / len(distances)
    max_distance = max(distances)
    min_distance = min(distances)

    return total_sum, avg, max_distance, min_distance