"""
QUESTION:
Create a function `classify_data` that takes in a 2D list `data` where each inner list represents a record with multiple attributes, and a list `weights` representing the attribute weights for each class (Class A, Class B, Class C). The function should return a list of classification results (Class A, Class B, or Class C) for each record.

Each attribute weight is a positive real number that affects the classification decision. The function should normalize the attribute values if necessary, calculate a classification score for each record, and classify each record based on the highest score.
"""

def classify_data(data, weights):
    """
    Classify a list of records into Class A, Class B, or Class C based on attribute weights.

    Args:
        data (list): A 2D list where each inner list represents a record with multiple attributes.
        weights (list): A list of attribute weights for each class (Class A, Class B, Class C).

    Returns:
        list: A list of classification results (Class A, Class B, or Class C) for each record.
    """

    # Initialize an empty list to store classification results
    classifications = []

    # Iterate over each record in the data
    for record in data:
        # Initialize scores for each class
        scoreA = 0
        scoreB = 0
        scoreC = 0

        # Calculate weighted sum for each class
        for i, attribute in enumerate(record):
            scoreA += attribute * weights[0][i]
            scoreB += attribute * weights[1][i]
            scoreC += attribute * weights[2][i]

        # Classify the record based on the highest score
        if scoreA > scoreB and scoreA > scoreC:
            classifications.append('Class A')
        elif scoreB > scoreA and scoreB > scoreC:
            classifications.append('Class B')
        else:
            classifications.append('Class C')

    return classifications