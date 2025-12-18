"""
QUESTION:
Everybody know that you passed to much time awake during night time...

Your task here is to define how much coffee you need to stay awake after your night. 
You will have to complete a function that take an array of events in arguments, according to this list you will return the number of coffee you need to stay awake during day time. **Note**: If the count exceed 3 please return 'You need extra sleep'.

The list of events can contain the following:

- You come here, to solve some kata ('cw').

- You have a dog or a cat that just decide to wake up too early ('dog' | 'cat').

- You just watch a movie ('movie').

- Other events can be present and it will be represent by arbitrary string, just ignore this one.

Each event can be downcase/lowercase, or uppercase. If it is downcase/lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.
"""

def calculate_coffee_needed(events):
    # Define the coffee requirements for each event type
    cs = {'cw': 1, 'CW': 2, 'cat': 1, 'CAT': 2, 'dog': 1, 'DOG': 2, 'movie': 1, 'MOVIE': 2}
    
    # Calculate the total number of coffees needed
    total_coffees = sum((cs.get(e, 0) for e in events))
    
    # Return the appropriate result based on the total number of coffees
    return 'You need extra sleep' if total_coffees > 3 else total_coffees