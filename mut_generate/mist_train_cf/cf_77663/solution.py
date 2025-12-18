"""
QUESTION:
Write a function called `is_symmetric_distribution` that determines whether a given distribution is symmetric around zero. The function should return `True` if the distribution is symmetric and `False` otherwise. The function should take as input a list of differences (a list of numbers).
"""

def is_symmetric_distribution(differences):
    # Count the occurrences of each absolute difference
    diff_counts = {}
    for diff in differences:
        key = abs(diff)
        if key in diff_counts:
            diff_counts[key] += 1
        else:
            diff_counts[key] = 1
    
    # Check if the counts are the same for positive and negative differences
    for key, count in diff_counts.items():
        pos_count = sum(1 for diff in differences if diff == key)
        neg_count = sum(1 for diff in differences if diff == -key)
        if pos_count != neg_count:
            return False
    
    return True