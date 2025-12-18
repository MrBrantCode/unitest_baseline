"""
QUESTION:
Design a function `update_voting_system` that updates the vote counts and comments in real-time based on new votes in a decentralized, real-time voting system interface built on Ethereum blockchain technology. The function should ensure continuous voter engagement and efficient data retrieval.
"""

def update_voting_system(vote_counts, comments, new_votes, new_comments):
    """
    Updates the vote counts and comments in real-time based on new votes.

    Args:
    vote_counts (dict): Current vote counts.
    comments (list): Current comments.
    new_votes (dict): New votes to be added.
    new_comments (list): New comments to be added.

    Returns:
    tuple: Updated vote counts and comments.
    """
    
    # Update vote counts
    for candidate, count in new_votes.items():
        if candidate in vote_counts:
            vote_counts[candidate] += count
        else:
            vote_counts[candidate] = count
    
    # Update comments
    comments.extend(new_comments)
    
    return vote_counts, comments