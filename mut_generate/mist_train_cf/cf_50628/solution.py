"""
QUESTION:
Create a function `feedback(score)` that takes an integer score as input and returns a string based on the following conditions: 
- 'Excellent!' if the score is 90 or above, 
- 'Good job!' if the score is between 70 (inclusive) and 89, 
- 'You need to improve' for all other scores.
"""

def feedback(score):
    return 'Excellent!' if score >= 90 else 'Good job!' if score >= 70 else 'You need to improve'