"""
QUESTION:
Write a function `generate_hyperparameter_combinations(ridge, sgd)` that generates all possible combinations of hyperparameters for the `ridge` and `sgd` models and returns them as a list of dictionaries. The input dictionaries `ridge` and `sgd` contain hyperparameter names as keys and lists of possible values as values. Each dictionary in the output list should represent a combination of hyperparameters for either the `ridge` or `sgd` model and should include the model name as the value for the 'model' key. The order of combinations in the output list does not matter.
"""

def generate_hyperparameter_combinations(ridge, sgd):
    def _cartesian_product(arrays):
        result = [[]]
        for array in arrays:
            new_result = []
            for x in result:
                for y in array:
                    new_result.append(x + [y])
            result = new_result
        return result

    def _generate_combinations(params_dict):
        keys = list(params_dict.keys())
        values = [params_dict[key] for key in keys]
        combinations = _cartesian_product(values)
        return [{keys[i]: combination[i] for i in range(len(keys))} for combination in combinations]

    ridge_combinations = [{'model': 'ridge', **params} for params in _generate_combinations(ridge)]
    sgd_combinations = [{'model': 'sgd', **params} for params in _generate_combinations(sgd)]
    return ridge_combinations + sgd_combinations