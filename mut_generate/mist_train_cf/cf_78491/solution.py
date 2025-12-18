"""
QUESTION:
Write a function `calculate_votes(A_votes)` that takes the number of votes Candidate A received as input. Given that Candidate A received 15% more votes than Candidate B, Candidate C received 20% less votes than Candidate A, Candidate D received the exact average number of votes received by candidates A, B, and C, and Candidate E received the sum of votes that Candidate B and D have got less by 1000, calculate and return the vote counts of Candidates B, C, D, and E, and the total vote count.
"""

def calculate_votes(A_votes):
    """
    Calculate the vote counts of Candidates B, C, D, and E, 
    and the total vote count given the number of votes Candidate A received.

    Args:
        A_votes (int): The number of votes Candidate A received.

    Returns:
        tuple: A tuple containing the vote counts of Candidates B, C, D, E, and the total vote count.
    """
    A = A_votes
    B = A * 100 / 115  # since A received 15% more votes than B
    C = A - (A * 0.2)  # since C received 20% less votes than A
    D = (A + B + C) / 3  # since D received exact average votes of A, B and C
    E = (B + D) - 1000  # since E received sum of B and D less by 1000
    Total = A + B + C + D + E 
    return B, C, D, E, Total