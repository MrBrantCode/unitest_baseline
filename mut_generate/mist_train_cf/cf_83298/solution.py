"""
QUESTION:
Create a function `classify_animals` that takes a list of animal names as input and classifies each animal into one of three categories: 'mammal', 'reptile', or 'bird', along with a subcategory of 'carnivore', 'herbivore', or 'omnivore'. The function should also provide a reason for each classification. The classification and reasons for each animal are predefined.
"""

class Animal:
    def __init__(self, category, subcategory, reason):
        self.category = category
        self.subcategory = subcategory
        self.reason = reason

def classify_animals(animal_names):
    animals = {
        'dog': Animal('mammal', 'carnivore', 'Dogs are normally meat eaters, and are mammals'),
        'snake': Animal('reptile', 'carnivore', 'Snakes eat other animals and belong to reptiles'),
        'turtle': Animal('reptile', 'herbivore', 'Most turtles are herbivores and they are reptiles'),
        'elephant': Animal('mammal', 'herbivore', 'Elephants eat plants and are mammals'),
        'eagle': Animal('bird', 'carnivore', 'Eagles eat other animals and are birds'),
        'rabbit': Animal('mammal', 'herbivore', 'Rabbits primarily eat plants and are mammals')
    }
    
    classified_animals = {}
    for name in animal_names:
        if name in animals:
            classified_animals[name] = animals[name]
    
    return classified_animals