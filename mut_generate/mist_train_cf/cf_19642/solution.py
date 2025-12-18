"""
QUESTION:
Write a function `calculate_votes` that takes two lists as input, `candidate_votes` and `ages`, where `candidate_votes` contains the number of votes for each candidate and `ages` contains the ages of the registered voters. The function should return the total number of votes for a candidate from registered voters who are aged 18-30. The function should ignore invalid ages (non-integer values, negative ages, or ages above 150) and only consider candidates with at least 1000 votes from registered voters aged 18-30.
"""

def calculate_votes(candidate_votes, ages):
    total_votes = 0
    
    # Iterate over each vote and age
    for vote, age in zip(candidate_votes, ages):
        # Check if age is valid
        if not isinstance(age, int) or age < 0 or age > 150:
            continue
        
        # Check if age is within the specified range
        if 18 <= age <= 30:
            total_votes += vote
    
    return total_votes