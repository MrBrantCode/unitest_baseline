"""
QUESTION:
Create a function `get_greeting` that takes an integer `hour` (ranging from 0 to 23) as input and returns a corresponding greeting based on the time of day. The function should have a time complexity of O(1) and must not use if-else or switch statements.
"""

def get_greeting(hour):
    greetings = {
        0: 'Good night',
        1: 'Good night',
        2: 'Good night',
        3: 'Good night',
        4: 'Good night',
        5: 'Good morning',
        6: 'Good morning',
        7: 'Good morning',
        8: 'Good morning',
        9: 'Good morning',
        10: 'Good morning',
        11: 'Good morning',
        12: 'Good afternoon',
        13: 'Good afternoon',
        14: 'Good afternoon',
        15: 'Good afternoon',
        16: 'Good afternoon',
        17: 'Good afternoon',
        18: 'Good evening',
        19: 'Good evening',
        20: 'Good evening',
        21: 'Good evening',
        22: 'Good evening',
        23: 'Good evening'
    }
    
    return greetings[hour]