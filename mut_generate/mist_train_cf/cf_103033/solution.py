"""
QUESTION:
Create a function called `unique_fruits` that takes a list of fruit names as input and returns a list containing each fruit only once. Ensure that the original order of fruits is maintained in the output.
"""

def unique_fruits(fruits):
    seen = set()
    unique = [fruit for fruit in fruits if not (fruit in seen or seen.add(fruit))]
    return unique