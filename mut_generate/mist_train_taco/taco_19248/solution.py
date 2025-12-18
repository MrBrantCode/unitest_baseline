"""
QUESTION:
To celebrate the start of the Rio Olympics (and the return of 'the Last Leg' on C4 tonight) this is an Olympic inspired kata.

Given a string of random letters, you need to examine each. Some letters naturally have 'rings' in them. 'O' is an obvious example, but 'b', 'p', 'e', 'A', etc are all just as applicable. 'B' even has two!! Please note for this kata you can count lower case 'g' as only one ring.

Your job is to count the 'rings' in each letter and divide the total number by 2. Round the answer down. Once you have your final score:

if score is 1 or less,  return 'Not even a medal!';
if score is 2, return 'Bronze!';
if score is 3, return 'Silver!';
if score is more than 3, return 'Gold!';

Dots over i's and any other letters don't count as rings.
"""

def calculate_medal(string: str) -> str:
    # Define the rings count for each letter
    ring_counts = {
        'a': 1, 'b': 1, 'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1, 'q': 1,
        'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1
    }
    
    # Calculate the total number of rings in the string
    total_rings = sum(ring_counts.get(char, 0) for char in string)
    
    # Divide the total number of rings by 2 and round down
    score = total_rings // 2
    
    # Determine the medal based on the score
    if score <= 1:
        return 'Not even a medal!'
    elif score == 2:
        return 'Bronze!'
    elif score == 3:
        return 'Silver!'
    else:
        return 'Gold!'