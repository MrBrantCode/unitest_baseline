"""
QUESTION:
In some ranking people collects points. The challenge is sort by points and calulate position for every person. But remember if two or more persons have same number of points, they should have same position number and sorted by name (name is unique).

For example:
Input structure:

Output should be:
"""

def calculate_rankings(people):
    # Sort the list of people by points in descending order and by name in ascending order
    people.sort(key=lambda x: (-x['points'], x['name']))
    
    # Calculate the position for each person
    for i, person in enumerate(people):
        if i == 0 or person['points'] < people[i - 1]['points']:
            person['position'] = i + 1
        else:
            person['position'] = people[i - 1]['position']
    
    return people