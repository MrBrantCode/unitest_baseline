"""
QUESTION:
Calculate the total number of votes Candidate B received and the total number of invalid votes over three days given the following conditions:

The function, calculate_election_results, takes a list of Candidate A's votes and a list of their corresponding percentages more than Candidate B's votes, as well as a list of percentages of invalid votes for each day.

For example, if Candidate A received 23,000, 26,000 and 30,000 votes and received 10%, 20%, and 30% more votes than Candidate B on each day, and 3%, 4%, and 5% of the total votes were declared invalid each day, the function should return the total number of votes Candidate B received and the total number of invalid votes.
"""

def calculate_election_results(cand_a_votes, cand_a_more_than_b_percentages, invalid_votes_percentages):
    total_cand_b_votes = 0
    total_invalid_votes = 0

    for i in range(len(cand_a_votes)):
        cand_b_votes = (cand_a_votes[i] * 100) / (100 + cand_a_more_than_b_percentages[i])
        total_cand_b_votes += cand_b_votes
        total_votes = cand_a_votes[i] + cand_b_votes
        total_invalid_votes += (total_votes * invalid_votes_percentages[i]) / 100

    return int(total_cand_b_votes), int(total_invalid_votes)