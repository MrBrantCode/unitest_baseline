"""
QUESTION:
Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.
"""

def get_seat_location(seat_number: str) -> str:
    # Define the sections of the plane
    front = list(range(1, 21))
    middle = list(range(21, 41))
    back = list(range(41, 61))
    
    # Define the seat clusters
    left = 'ABC'
    center = 'DEF'
    right = 'GHK'
    
    # Extract the number and letter from the seat_number
    seat_num = int(seat_number[:-1])
    seat_letter = seat_number[-1]
    
    # Determine the section of the plane
    section = ''
    if seat_num in front:
        section = 'Front-'
    elif seat_num in middle:
        section = 'Middle-'
    elif seat_num in back:
        section = 'Back-'
    else:
        return 'No Seat!!'
    
    # Determine the cluster of the seat
    cluster = ''
    if seat_letter in left:
        cluster = 'Left'
    elif seat_letter in center:
        cluster = 'Middle'
    elif seat_letter in right:
        cluster = 'Right'
    else:
        return 'No Seat!!'
    
    # Return the combined section and cluster
    return section + cluster