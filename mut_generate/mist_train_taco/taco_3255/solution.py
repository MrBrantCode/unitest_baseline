"""
QUESTION:
In Russia regular bus tickets usually consist of 6 digits. The ticket is called lucky when the sum of the first three digits equals to the sum of the last three digits. Write a function to find out whether the ticket is lucky or not. Return true if so, otherwise return false. Consider that input is always a string. Watch examples below.
"""

def is_lucky_ticket(ticket: str) -> bool:
    """
    Determines if a given 6-digit ticket number is lucky.

    A ticket is considered lucky if the sum of the first three digits
    equals the sum of the last three digits.

    Parameters:
    ticket (str): A 6-digit string representing the ticket number.

    Returns:
    bool: True if the ticket is lucky, False otherwise.
    """
    if len(ticket) == 6 and ticket.isdigit():
        digits = list(map(int, ticket))
        return sum(digits[:3]) == sum(digits[3:])
    return False