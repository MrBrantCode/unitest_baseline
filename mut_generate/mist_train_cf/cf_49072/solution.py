"""
QUESTION:
Create a function named `calculate_jaccard` that takes two sets of real numbers (which can be multidimensional, e.g., sets of tuples) as input and returns their Jaccard similarity coefficient and Jaccard distance. If the union of the sets is empty, the function should return a message indicating that division by zero is not possible.
"""

def calculate_jaccard(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union==0:
        return "Cannot divide by zero"
    else:
        jaccard_similarity = intersection / union
        jaccard_distance = 1 - jaccard_similarity
        return jaccard_similarity, jaccard_distance