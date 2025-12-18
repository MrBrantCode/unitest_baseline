"""
QUESTION:
Write a function `classify_particle` that combines multiple observations of a particle to extract new features and classify it into one of several classes. The function should take as input a list of observations, where each observation is a 2D representation of the particle in a frame. The function should return the predicted class of the particle. The function should be able to handle a variable number of observations.
"""

def classify_particle(observations):
    """
    Classify a particle based on multiple observations.

    Parameters:
    observations (list): A list of 2D representations of the particle in different frames.

    Returns:
    str: The predicted class of the particle.
    """

    # For simplicity, let's assume we're using a simple ensemble method
    # with a basic classifier for each view. In a real-world application,
    # you would replace this with a more sophisticated model.

    # Define a basic classifier function
    def classify_view(view):
        # Replace this with your actual classification logic
        # For demonstration purposes, let's assume we're classifying based on the sum of the view
        return "Class 1" if sum(sum(row) for row in view) > 10 else "Class 2"

    # Classify each view and store the results
    classifications = [classify_view(view) for view in observations]

    # Use a simple voting system to determine the final classification
    from collections import Counter
    final_classification = Counter(classifications).most_common(1)[0][0]

    return final_classification