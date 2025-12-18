"""
QUESTION:
Write a function `evaluate_model_selection` that determines whether cross-validation or a validation set is more suitable for a given dataset size and required level of precision. The function should take two parameters: `dataset_size` and `required_precision`. It should return a string stating whether cross-validation or a validation set is more suitable.
"""

def evaluate_model_selection(dataset_size, required_precision):
    if dataset_size < 1000:
        return "cross-validation"
    elif required_precision > 0.95:
        return "cross-validation"
    else:
        return "a validation set"