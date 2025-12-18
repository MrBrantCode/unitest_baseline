"""
QUESTION:
Write a function `generate_hyperparameter_combinations(hyperparameters)` that generates all possible combinations of hyperparameters for two machine learning models, 'random_forest' and 'xgboost_mat', from a given dictionary `hyperparameters`. The function should return a list of dictionaries, where each dictionary represents a unique combination of hyperparameters for the two models. The 'class_weight' for both models is always set to 'balanced'. 

The input dictionary `hyperparameters` has the following structure:
```python
hyperparameters = {
    'random_forest': {
        'hyperparameter1': [value1, value2, ...],
        'hyperparameter2': [value1, value2, ...],
        ...
    },
    'xgboost_mat': {
        'hyperparameter1': [value1, value2, ...],
        'hyperparameter2': [value1, value2, ...],
        ...
    }
}
```
Each dictionary in the output list should have the following structure:
```python
{
    'model': 'model_name',
    'hyperparameter1': value,
    'hyperparameter2': value,
    ...
}
```
Note that the function should generate all possible combinations of hyperparameters for both models, including the 'class_weight' parameter, which is always set to 'balanced'.
"""

from itertools import product

def entrance(hyperparameters):
    combinations = []
    for model, params in hyperparameters.items():
        keys = list(params.keys())
        values = [params[key] for key in keys]
        for combination in product(*values):
            combination_dict = {'model': model, 'class_weight': 'balanced'}
            for i in range(len(keys)):
                combination_dict[keys[i]] = combination[i]
            combinations.append(combination_dict)
    return combinations