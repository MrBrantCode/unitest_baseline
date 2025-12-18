"""
QUESTION:
Implement a function `classify_animals` that takes a list of animals as input and returns a dictionary with two keys: "mammal" and "reptile". The function should categorize the input animals into these two categories, removing duplicates, and raise an exception if the input list is empty. Assume the function has prior knowledge of animal classifications, specifically that "dog" and "elephant" are mammals, and "snake" and "turtle" are reptiles.
"""

def classify_animals(animals):
    if not animals:
        raise Exception("Input list is empty.")
    
    animal_dict = {"mammal": [], "reptile": []}
    
    for animal in animals:
        if animal not in animal_dict["mammal"] and animal not in animal_dict["reptile"]:
            if animal in ["dog", "elephant"]:
                animal_dict["mammal"].append(animal)
            elif animal in ["snake", "turtle"]:
                animal_dict["reptile"].append(animal)
    
    return animal_dict