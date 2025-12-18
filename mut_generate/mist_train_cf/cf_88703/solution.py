"""
QUESTION:
Write a function `calculate_votes(candidate, votes, ages)` that calculates the total number of votes for a candidate in an election from registered voters aged 18-30. The function should take in three parameters: `candidate`, a string representing the name of the candidate; `votes`, a list of integers representing the votes for the candidate; and `ages`, a list of integers representing the ages of the registered voters. The function should only consider votes from valid ages (integers between 18 and 30 inclusive), and should return a dictionary with the total number of votes for each candidate who has at least 1000 votes from valid ages.
"""

def calculate_votes(candidate, votes, ages):
    total_votes = {}
    
    for vote, age in zip(votes, ages):
        if isinstance(age, int) and 18 <= age <= 30:
            if candidate not in total_votes:
                total_votes[candidate] = 0
            total_votes[candidate] += vote
    
    total_votes = {c: v for c, v in total_votes.items() if v >= 1000}
    
    return total_votes