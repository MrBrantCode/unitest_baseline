"""
QUESTION:
Three candidates take part in a TV show.

In order to decide who will take part in the final game and probably become rich, they have to roll the Wheel of Fortune!

The Wheel of Fortune is divided into 20 sections, each with a number from 5 to 100 (only mulitples of 5).

Each candidate can roll the wheel once or twice and sum up the score of each roll.
The winner one that is closest to 100 (while still being lower or equal to 100). 
In case of a tie, the candidate that rolled the wheel first wins.

You receive the information about each candidate as an array of objects: each object should have a `name` and a `scores` array with the candidate roll values.

Your solution should return the name of the winner or `false` if there is no winner (all scored more than 100).

__Example:__

```python
c1 = {"name": "Bob", "scores": [10, 65]}
c2 = {"name": "Bill", "scores": [90, 5]}
c3 = {"name": "Charlie", "scores": [40, 55]}
winner([c1, c2, c3]) #Returns "Bill"
```

Please note that inputs may be invalid: in this case, the function should return false.

Potential errors derived from the specifications are:
- More or less than three candidates take part in the game.
- A candidate did not roll the wheel or rolled it more than twice.
- Scores are not valid.
- Invalid user entry (no name or no score).
"""

def determine_winner(candidates):
    try:
        # Validate the number of candidates
        assert len(candidates) == 3
        
        max_total = 0
        winner_name = None
        
        for candidate in candidates:
            name = candidate['name']
            scores = candidate['scores']
            
            # Validate the number of rolls and the scores
            assert 1 <= len(scores) <= 2
            assert all(s % 5 == 0 and 5 <= s <= 100 for s in scores)
            
            total = sum(scores)
            
            # Check if this candidate's total is the closest to 100 without exceeding it
            if max_total < total <= 100:
                winner_name = name
                max_total = total
        
        return winner_name if winner_name else False
    
    except (AssertionError, KeyError, TypeError):
        return False