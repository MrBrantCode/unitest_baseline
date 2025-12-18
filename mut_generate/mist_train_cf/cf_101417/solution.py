"""
QUESTION:
Create a function `recommend_treatment` that takes in three parameters: a dictionary `conditions` where the keys are medical conditions and the values are lists of treatments, a list of dictionaries `individuals` where each dictionary contains the personal information of an individual, and a function `calculate_bmi` that calculates BMI given height and weight.

The function should filter the list of individuals based on their occupation, calculate the BMI of each individual, and recommend the most effective treatment for their medical condition based on the treatment with the highest success rate for individuals in their occupation with a similar BMI. If no such data is available, the function should recommend the treatment with the highest overall success rate for that condition.

The function should return a dictionary where the keys are the names of individuals and the values are their recommended treatments.
"""

def recommend_treatment(conditions, individuals, calculate_bmi, success_rates_by_occupation_bmi, overall_success_rates):
    # Filter individuals by occupation
    doctors = [i for i in individuals if i.get("occupation") == "Doctor"]
    
    # Create dictionary to store recommended treatments for each individual
    recommendations = {}
    
    for individual in doctors:
        # Calculate BMI
        bmi = calculate_bmi(individual.get("height"), individual.get("weight"))
        
        for condition, treatments in conditions.items():
            # Find success rates for condition in individual's occupation and BMI range
            success_rates = success_rates_by_occupation_bmi(condition, individual.get("occupation"), bmi)
            if success_rates:
                # Find treatment with highest success rate in range
                best_treatment = max(success_rates, key=success_rates.get)
            else:
                # Find treatment with highest overall success rate
                overall_success_rates_for_condition = overall_success_rates(condition)
                best_treatment = max(overall_success_rates_for_condition, key=overall_success_rates_for_condition.get)
            
            # Add recommended treatment to dictionary
            recommendations[individual.get("name")] = best_treatment
    
    return recommendations