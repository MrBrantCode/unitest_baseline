"""
QUESTION:
Given an array (or list) of scores, return the array of _ranks_ for each value in the array.  The largest value has rank 1, the second largest value has rank 2, and so on. Ties should be handled by assigning the same rank to all tied values. For example:

    ranks([9,3,6,10]) = [2,4,3,1]

and

    ranks([3,3,3,3,3,5,1]) = [2,2,2,2,2,1,7]
    
because there is one 1st place value, a five-way tie for 2nd place, and one in 7th place.
"""

def calculate_ranks(scores):
    # Create a sorted list of scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    
    # Create a dictionary to map each score to its rank
    rank_dict = {}
    current_rank = 1
    
    for score in sorted_scores:
        if score not in rank_dict:
            rank_dict[score] = current_rank
        current_rank += 1
    
    # Create the list of ranks based on the original scores
    ranks = [rank_dict[score] for score in scores]
    
    return ranks