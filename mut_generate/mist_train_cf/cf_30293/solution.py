"""
QUESTION:
Implement a function `calculate_molecular_weight(compound: str, atomic_weights: dict) -> float` that calculates the molecular weight of a chemical compound. The `compound` string represents the chemical compound where each element is represented by its chemical symbol followed by an optional integer indicating the number of atoms of that element. The `atomic_weights` dictionary contains the atomic weights of the elements, where each key is an element's chemical symbol and its corresponding value is the atomic weight. If an element in the compound is not present in the `atomic_weights` dictionary, ignore that element and continue the calculation. The chemical symbols in the `compound` string consist of uppercase letters only.
"""

def calculate_molecular_weight(compound: str, atomic_weights: dict) -> float:
    weight = 0.0
    current_element = ""
    current_count = 0

    for char in compound:
        if char.isalpha():
            if current_element:
                weight += atomic_weights.get(current_element, 0) * max(current_count, 1)
                current_element = char
                current_count = 0
            else:
                current_element = char
        else:
            current_count = current_count * 10 + int(char)

    if current_element:
        weight += atomic_weights.get(current_element, 0) * max(current_count, 1)

    return weight