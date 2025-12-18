"""
QUESTION:
Implement the `get_vector_model` function that takes a language parameter `lang` and returns a dictionary representing the vector model for the specified language. The vector model maps words to their corresponding vectors, where each vector is a list of numerical values. If the specified language is not recognized, return an empty dictionary.
"""

def get_vector_model(lang):
    if lang == "english":
        return {
            "apple": [0.5, 0.3, 0.8],
            "banana": [0.4, 0.6, 0.2],
            "orange": [0.7, 0.5, 0.1]
        }
    elif lang == "french":
        return {
            "pomme": [0.6, 0.4, 0.7],
            "banane": [0.3, 0.7, 0.5],
            "orange": [0.8, 0.2, 0.6]
        }
    else:
        return {}