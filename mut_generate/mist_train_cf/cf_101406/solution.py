"""
QUESTION:
Implement a function `contact_tracing(infected_people, locations)` that identifies people who may have come into contact with an infected person. The function takes in a list of `infected_people` and a dictionary `locations` where the keys are the names of people and the values are lists of locations they have visited. The function should return a set of people who may have been in close contact with the infected individuals.
"""

def trace_contacts(infected_people, locations):
    contacts = []
    for person in infected_people:
        for location in locations[person]:
            for other_person, other_locations in locations.items():
                if person != other_person and location in other_locations:
                    contacts.append(other_person)
    return set(contacts)