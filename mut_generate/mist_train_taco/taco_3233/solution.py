"""
QUESTION:
In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:
```
003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
```
Such tickets were either eaten after being used or collected for bragging rights.

Your task is to write a funtion ```luck_check(str)```, which returns ```true/True``` if argument is string decimal representation of a lucky ticket number, or ```false/False``` for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.
"""

def is_lucky_ticket(ticket_number: str) -> bool:
    # Check if the input string is empty
    if not ticket_number:
        raise ValueError("Ticket number cannot be empty")
    
    # Check if the input string contains only digits
    if not ticket_number.isdigit():
        raise ValueError("Ticket number must contain only decimal digits")
    
    # Calculate the midpoint indices
    length = len(ticket_number)
    mid_left = length // 2
    mid_right = (length + 1) // 2
    
    # Calculate the sum of the left half and the right half
    left_sum = sum(int(digit) for digit in ticket_number[:mid_left])
    right_sum = sum(int(digit) for digit in ticket_number[mid_right:])
    
    # Check if the sums are equal
    return left_sum == right_sum