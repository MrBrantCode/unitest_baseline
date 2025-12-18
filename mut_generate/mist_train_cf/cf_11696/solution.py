"""
QUESTION:
Write a function `count_votes(votes)` that takes a list of tuples `votes` as input, where each tuple contains a candidate's name (a string of only uppercase letters, max length 10) and the number of votes (a positive integer, max 1000). The function should return a dictionary containing the candidate names as keys and their corresponding vote counts as values, but only if the total number of votes is at least 100. If the total number of votes is less than 100, or if any candidate's name or vote count is invalid, the function should return an empty dictionary.
"""

def count_votes(votes):
    result = {}
    total_votes = 0

    # Calculate total number of votes
    for vote in votes:
        candidate_name, num_votes = vote
        total_votes += num_votes

    # Check if the total number of votes is at least 100
    if total_votes < 100:
        return result

    # Calculate vote count for each candidate
    for vote in votes:
        candidate_name, num_votes = vote

        # Check candidate name length and format
        if len(candidate_name) > 10 or not candidate_name.isupper():
            return result

        # Check number of votes
        if num_votes < 1 or num_votes > 1000:
            return result

        # Add candidate and vote count to result dictionary
        result[candidate_name] = num_votes

    return result