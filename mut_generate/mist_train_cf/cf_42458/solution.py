"""
QUESTION:
Create a Python function `calculate_monthly_debt` that takes three parameters: `region` (string), `annual_income` (integer), and `sat_scores` (list of integers). The function should use a predefined model dictionary to make predictions based on the SAT scores and adjust the prediction based on the annual income. The adjustment rules are: if the annual income is less than $30,001, add `low_income_dif` to the prediction; if the annual income is between $30,001 and $75,000, add `mid_income_dif` to the prediction. The function should return a dictionary with the key "total_debt" and the adjusted prediction as the value.
"""

def calculate_monthly_debt(region: str, annual_income: int, sat_scores: list):
    model_dict = {
        'sat': {
            'newyork': {
                'high': {'coefficients': [0.5, 1, 0.8], 'intercept': 100}
            },
            # Add models for other regions and levels as needed
        }
    }
    low_income_dif = 50  # Example adjustment for low income
    mid_income_dif = 30  # Example adjustment for mid income

    def flatten_prediction(scores, model):
        prediction = model['intercept']
        for i in range(len(scores)):
            prediction += scores[i] * model['coefficients'][i]
        return prediction

    model_to_use = model_dict['sat'][region]['high']
    prediction = flatten_prediction(sat_scores, model_to_use)

    if annual_income < 30001:
        prediction += low_income_dif
    elif 30000 < annual_income < 75001:
        prediction += mid_income_dif

    return {"total_debt": int(prediction)}