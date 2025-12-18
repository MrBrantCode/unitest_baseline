"""
QUESTION:
A group of friends (n >= 2) have reunited for a get-together after 
a very long time. 

They agree that they will make presentations on holiday destinations 
or expeditions they have been to only if it satisfies **one simple rule**: 
> the holiday/journey being presented must have been visited _only_ by the presenter and no one else from the audience.

Write a program to output the presentation agenda, including the
presenter and their respective presentation titles. 

---
### EXAMPLES

```python
presentation_agenda([
    {'person': 'Abe', 'dest': ['London', 'Dubai']},
    {'person': 'Bond', 'dest': ['Melbourne', 'Dubai']}
]) == [{'person': 'Abe', 'dest': ['London']},
       {'person': 'Bond', 'dest': ['Melbourne']}]

presentation_agenda([
    {'person': 'Abe', 'dest': ['Dubai']},
    {'person': 'Brad', 'dest': ['Dubai']}
]) == []

presentation_agenda([
    {'person': 'Abe', 'dest': ['London', 'Dubai']},
    {'person': 'Bond', 'dest': ['Melbourne', 'Dubai']},
    {'person': 'Carrie', 'dest': ['Melbourne']},
    {'person': 'Damu', 'dest': ['Melbourne', 'Dubai', 'Paris']}
]) == [{'person': 'Abe',  'dest': ['London']},
       {'person': 'Damu', 'dest': ['Paris']}]

```
"""

from collections import Counter

def generate_presentation_agenda(friend_list):
    # Step 1: Count the occurrences of each destination
    destination_counts = Counter(d for p in friend_list for d in p['dest'])
    
    # Step 2: Identify unique destinations (those visited by only one person)
    unique_destinations = {d for d, c in destination_counts.items() if c == 1}
    
    # Step 3: Filter each friend's destinations to include only unique ones
    filtered_presentations = [
        {'person': p['person'], 'dest': [d for d in p['dest'] if d in unique_destinations]}
        for p in friend_list
    ]
    
    # Step 4: Remove any presentations with empty destinations
    return [p for p in filtered_presentations if p['dest']]