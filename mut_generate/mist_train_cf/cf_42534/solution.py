"""
QUESTION:
Given the lucky number and a list of ticket numbers, write a function `find_winning_ticket` that returns the winning ticket number, which is the number closest to the lucky number. If multiple tickets have the same closest distance to the lucky number, the function should return the one with the smallest ticket number. The function should take three parameters: the lucky number (an integer), the number of tickets sold (an integer), and the ticket numbers (an array of integers).
"""

def find_winning_ticket(lucky_number, num_tickets, ticket_numbers):
    closest_distance = float('inf')
    winning_ticket = float('inf')

    for ticket in ticket_numbers:
        distance = abs(ticket - lucky_number)
        if distance < closest_distance or (distance == closest_distance and ticket < winning_ticket):
            closest_distance = distance
            winning_ticket = ticket

    return winning_ticket