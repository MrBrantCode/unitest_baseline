"""
QUESTION:
Create a function `get_model_confidence(models, model_name)` that takes a dictionary `models` containing machine learning model information and a `model_name` string as input, and returns the confidence level of the specified model as a percentage string. If the model is not found in the dictionary or the confidence level is missing, return a corresponding error message. The confidence level in the dictionary is represented as a decimal number between 0 and 1.
"""

def entrance(models, model_name):
    if model_name in models and 'confidence' in models[model_name]:
        confidence_decimal = models[model_name]['confidence']
        confidence_percentage = int(confidence_decimal * 100)
        return f"{confidence_percentage}%"
    else:
        return "Model not found or confidence level missing"