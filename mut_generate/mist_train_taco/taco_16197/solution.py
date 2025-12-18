"""
QUESTION:
You've just recently been hired to calculate scores for a  Dart Board game!

Scoring specifications:

* 0 points - radius above 10
* 5 points - radius between 5 and 10 inclusive
* 10 points - radius less than 5

**If all radii are less than 5, award 100 BONUS POINTS!**

Write a function that accepts an array of radii (can be integers and/or floats), and returns a total score using the above specification.

An empty array should return 0.

## Examples:
"""

def calculate_dart_score(radiuses):
    score = 0
    for r in radiuses:
        if r < 5:
            score += 10
        elif 5 <= r <= 10:
            score += 5
    
    if radiuses and max(radiuses) < 5:
        score += 100
    
    return score