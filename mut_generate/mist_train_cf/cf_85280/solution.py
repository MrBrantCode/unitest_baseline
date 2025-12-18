"""
QUESTION:
Create a function named `sort_entities` that sorts an array of entities in descending order based on their measurements (age). If two entities have the same measurement, sort them lexicographically based on their identities (name). Implement a custom sorting algorithm without using built-in sorting libraries. The input is an array of entities where each entity has a name and a measurement, and the output is an array of entity names in the sorted order.
"""

class Entity:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def sort_entities(entities):
    for i in range(len(entities)-1):
        for j in range(len(entities)-i-1):
            if entities[j].age < entities[j + 1].age:
                entities[j], entities[j + 1] = entities[j + 1], entities[j]
            elif entities[j].age == entities[j + 1].age:
                if entities[j].name > entities[j + 1].name:
                    entities[j], entities[j + 1] = entities[j + 1], entities[j]
    return [entity.name for entity in entities]