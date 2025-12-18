"""
QUESTION:
Calculate the hypervolume of a tesseract given its side length. The tesseract is a regular convex polytope where all edges and angles are equal. 

Restrictions: The input side length should be a non-negative real number.
"""

def tesseract_hypervolume(side_length):
    """Calculate the hypervolume of a tesseract given the side length."""
    hypervolume = side_length ** 4
    return hypervolume