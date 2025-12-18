"""
QUESTION:
Create a function `calculate_election_results(votes)` that takes a list of votes as input, where each vote is a tuple in the format `(candidate_name, number_of_votes)`. The function should return a dictionary containing the candidate names as keys and their corresponding vote counts and percentages as values. The candidate names must be strings consisting of only uppercase letters with a maximum length of 10 characters, and the number of votes must be a positive integer not exceeding 1000. The total number of votes must be at least 100. The percentage of votes for each candidate should be calculated and rounded to two decimal places. If the total number of votes is less than 100, the function should return an error message and `None`.
"""

def calculate_election_results(votes):
    # Initialize dictionary to store results
    results = {}

    # Calculate total number of votes
    total_votes = 0
    for vote in votes:
        total_votes += vote[1]

    # Check if total number of votes is at least 100
    if total_votes < 100:
        print("Error: Total number of votes must be at least 100.")
        return None

    # Calculate and store results
    for vote in votes:
        candidate_name = vote[0]
        number_of_votes = vote[1]
        percentage = (number_of_votes / total_votes) * 100
        percentage = round(percentage, 2)
        results[candidate_name] = {
            'votes': number_of_votes,
            'percentage': percentage
        }

    return results