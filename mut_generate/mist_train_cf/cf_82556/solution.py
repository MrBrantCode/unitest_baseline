"""
QUESTION:
Design a function `predict_disease` that takes a list of user-provided symptoms as input and returns a predicted disease based on the symptoms. The function should utilize a predefined database of diseases and their associated symptoms. The database should not be created within the function, but rather be a separate entity that the function can access.
"""

def predict_disease(symptoms, disease_database):
    """
    Predicts a disease based on the provided symptoms.

    Args:
        symptoms (list): A list of user-provided symptoms.
        disease_database (dict): A dictionary containing diseases and their associated symptoms.

    Returns:
        str: The predicted disease.
    """
    # Initialize a dictionary to store the count of matched symptoms for each disease
    disease_match_count = {disease: 0 for disease in disease_database}

    # Iterate over each disease and its symptoms in the database
    for disease, disease_symptoms in disease_database.items():
        # Iterate over each user-provided symptom
        for symptom in symptoms:
            # Check if the symptom is associated with the current disease
            if symptom in disease_symptoms:
                # Increment the match count for the disease
                disease_match_count[disease] += 1

    # Find the disease with the most matched symptoms
    predicted_disease = max(disease_match_count, key=disease_match_count.get)

    return predicted_disease