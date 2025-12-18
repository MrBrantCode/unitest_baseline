"""
QUESTION:
Implement a function `validate_view_id(view_id: str) -> bool` that validates a given view ID based on the following rules:
- The view ID must be exactly 4 characters long.
- The first two characters must be digits between 01 and 12, representing the month.
- The last two characters must be digits between 01 and 31, representing the day.
The function should return `True` if the view ID meets the specified criteria and `False` otherwise.
"""

def entance(view_id: str) -> bool:
    if len(view_id) != 4:
        return False  

    month = int(view_id[:2])
    day = int(view_id[2:])

    if not (1 <= month <= 12):
        return False  

    if not (1 <= day <= 31):
        return False  

    return True 