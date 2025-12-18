"""
QUESTION:
Create a function `classify_data` that takes three inputs: `data_set`, a list of records where each record is a dictionary containing attribute-value pairs, `attribute_weights`, a dictionary containing attribute-weight pairs where the sum of all attribute weights equals 1, and `class_labels`, a list of three predefined classes ['Class A', 'Class B', 'Class C']. The function should return a list of tuples, where each tuple contains a record and its corresponding class label, based on the classification process described above.
"""

def classify_data(data_set, attribute_weights, class_labels):
    """
    This function classifies the given data into three predefined classes based on multiple criteria.

    Args:
    - data_set (list): A list of records, where each record is a dictionary containing attribute-value pairs.
    - attribute_weights (dict): A dictionary containing attribute-weight pairs.
    - class_labels (list): A list of the predefined classes.

    Returns:
    - classification_result (list): A list of tuples, where each tuple contains the record and its corresponding class label.
    """

    # Calculate the sum of all attribute weights
    weight_sum = sum(attribute_weights.values())

    # Normalize the attribute weights
    attribute_weights = {key: value / weight_sum for key, value in attribute_weights.items()}

    classification_result = []
    
    for record in data_set:
        class_scores = {class_label: 0 for class_label in class_labels}
        
        for attribute, value in record.items():
            if attribute in attribute_weights:
                class_scores[class_labels[0]] += value * attribute_weights[attribute]
                class_scores[class_labels[1]] += value * attribute_weights[attribute]
                class_scores[class_labels[2]] += value * attribute_weights[attribute]

        max_score = max(class_scores.values())
        max_class = [class_label for class_label, score in class_scores.items() if score == max_score][0]

        classification_result.append((record, max_class))

    return classification_result