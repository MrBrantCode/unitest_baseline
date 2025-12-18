"""
QUESTION:
Write a function named `contact_tracing` that takes two parameters: a list of infected people and a dictionary of locations each person has visited. The function should return a set of people who may have come into contact with an infected person.

The function should iterate through each infected person and their locations, then check if any other person has visited the same location. If so, that person should be added to the set of contacts.

The function should return a set of unique people who may have come into contact with an infected person.
"""

def contact_tracing(infected_people, locations):
    contacts = set()
    for person in infected_people:
        for location in locations[person]:
            for other_person, other_locations in locations.items():
                if person != other_person and location in other_locations:
                    contacts.add(other_person)
    return contacts