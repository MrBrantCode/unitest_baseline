"""
QUESTION:
Implement a function `find_auction_winner(people: dict) -> str` that determines the winner(s) of a silent auction. The function takes a dictionary `people` as input, where the keys are participant names and the values are their respective bids. It should return the name of the single winner if there is no tie, or a list of names in case of a tie for the highest bid.
"""

def find_auction_winner(people: dict) -> str:
    max_bid = max(people.values())
    winners = [person for person, bid in people.items() if bid == max_bid]
    if len(winners) == 1:
        return winners[0]
    else:
        return winners