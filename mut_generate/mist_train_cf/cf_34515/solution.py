"""
QUESTION:
Implement the `select_prize_winners` function, which takes a list of tickets and a conference as input. Each ticket contains information about the attendee, including their name, email, and a unique identifier (slug). The function should select prize winners based on the following conditions: 
1. The attendee must have provided an email address.
2. The ticket must not have been used to select a prize winner before.

The function should return a list of PrizeWinner objects, each containing the name and email of the selected prize winners. 

Function signature: `def select_prize_winners(tickets: List[Dict[str, Union[str, int]]], conf: Conference) -> List[PrizeWinner]`
"""

from typing import List, Dict, Union

class PrizeWinner:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

def select_prize_winners(tickets: List[Dict[str, Union[str, int]]]) -> List[PrizeWinner]:
    """
    Selects prize winners based on the provided tickets.

    Args:
    tickets (List[Dict[str, Union[str, int]]]): A list of tickets, each containing information about the attendee.

    Returns:
    List[PrizeWinner]: A list of PrizeWinner objects, each containing the name and email of the selected prize winners.
    """
    winners = []
    used_slugs = set()
    
    for ticket in tickets:
        if 'email' in ticket and ticket['email'] and 'slug' in ticket and ticket['slug'] not in used_slugs:
            used_slugs.add(ticket['slug'])
            winners.append(PrizeWinner(ticket['name'], ticket['email']))
    
    return winners