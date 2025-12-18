"""
QUESTION:
Create a function called `count_votes` that takes a list of votes as input, where each vote is a tuple `(candidate_name, number_of_votes)`. The function should return a dictionary containing the candidate names as keys and their corresponding vote counts and percentages as values, as well as the total number of votes and the winner(s) of the election. The candidate names should be strings consisting of only uppercase letters with a maximum length of 10 characters, and the number of votes should be positive integers not exceeding 1000. The total number of votes should be at least 100. If there are multiple candidates with the same highest number of votes, the function should indicate a tie in the output. The percentages should be rounded to two decimal places.
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