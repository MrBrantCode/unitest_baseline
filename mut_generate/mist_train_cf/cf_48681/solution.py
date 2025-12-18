"""
QUESTION:
Write a function `get_name_score` that takes a list of names as input, calculates the alphabetical value of each name by summing the alphabetical positions of its characters (A=1, B=2, ..., Z=26), multiplies each alphabetical value by its 1-indexed position in the sorted list, and returns the sum of all the resulting name scores. The input list should be in lexicographical order.
"""

def get_name_score(name_list):
    # Calculate alphabetical worth of a name
    def get_alphabetical_value(name):
        return sum(ord(i) - 64 for i in name) # 'A' is 65 in ASCII, so 'A' - 64 gives the alphabetical value 1.

    # Compute score of each name
    scores = [(idx + 1) * get_alphabetical_value(name) for idx, name in enumerate(name_list)]
    
    # Return total score
    return sum(scores)