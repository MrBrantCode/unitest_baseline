"""
QUESTION:
Create a function `count_votes` that takes a list of votes as input, where each vote is a tuple `(candidate_name, number_of_votes)`, and returns a dictionary with the election results. The candidate names must be strings of uppercase letters with a maximum length of 10 characters, and the number of votes must be a positive integer not exceeding 1000. The total number of votes must be at least 100. The output dictionary should contain the candidate names as keys and their corresponding vote counts and percentages as values, as well as the total number of votes and the winner(s) of the election. If there is a tie, the function should indicate this in the output dictionary.
"""

def count_votes(votes):
    candidates = {}
    total_votes = 0
    highest_votes = 0
    highest_candidates = []

    for candidate, votes_count in votes:
        if candidate not in candidates:
            candidates[candidate] = votes_count
        else:
            candidates[candidate] += votes_count

        total_votes += votes_count

        if candidates[candidate] > highest_votes:
            highest_votes = candidates[candidate]
            highest_candidates = [candidate]
        elif candidates[candidate] == highest_votes:
            highest_candidates.append(candidate)

    results = {}

    for candidate, votes_count in candidates.items():
        percentage = round((votes_count / total_votes) * 100, 2)
        results[candidate] = {'votes': votes_count, 'percentage': percentage}

    results['total_votes'] = total_votes

    if len(highest_candidates) > 1:
        results['winner'] = 'Tie'
        results['highest_votes'] = highest_votes
    else:
        results['winner'] = highest_candidates[0]
        results['highest_votes'] = highest_votes

    return results