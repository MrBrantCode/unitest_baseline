"""
QUESTION:
Write a function called compare_patient_groups to compare two groups of patients (hospitalized and non-hospitalized) based on a laboratory parameter with gender-specific reference values. The function should account for the interaction between the laboratory parameter and gender, and return a result that can be used for comparison between the two groups.
"""

def compare_patient_groups(hospitalized, non_hospitalized, lab_parameter, gender_specific_references):
    """
    Compare two groups of patients based on a laboratory parameter with gender-specific reference values.

    Parameters:
    hospitalized (list): List of patients who are hospitalized.
    non_hospitalized (list): List of patients who are not hospitalized.
    lab_parameter (str): The laboratory parameter to compare.
    gender_specific_references (dict): Dictionary with gender-specific reference values for the laboratory parameter.

    Returns:
    dict: A dictionary with the comparison result.
    """

    # Initialize the result dictionary
    result = {"hospitalized": {}, "non_hospitalized": {}}

    # Iterate over the gender-specific references
    for gender, reference in gender_specific_references.items():
        # Calculate the z-scores for the hospitalized patients
        hospitalized_z_scores = [patient[lab_parameter] / reference for patient in hospitalized if patient["gender"] == gender]
        # Calculate the z-scores for the non-hospitalized patients
        non_hospitalized_z_scores = [patient[lab_parameter] / reference for patient in non_hospitalized if patient["gender"] == gender]

        # Calculate the mean z-scores for the hospitalized and non-hospitalized patients
        hospitalized_mean_z_score = sum(hospitalized_z_scores) / len(hospitalized_z_scores) if hospitalized_z_scores else 0
        non_hospitalized_mean_z_score = sum(non_hospitalized_z_scores) / len(non_hospitalized_z_scores) if non_hospitalized_z_scores else 0

        # Store the comparison result in the result dictionary
        result["hospitalized"][gender] = hospitalized_mean_z_score
        result["non_hospitalized"][gender] = non_hospitalized_mean_z_score

    return result