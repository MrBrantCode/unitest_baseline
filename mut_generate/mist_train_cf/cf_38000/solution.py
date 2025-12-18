"""
QUESTION:
Write a function `find_best_models` that takes in three dictionaries: `model_results`, `model_types`, and `datasets`. The function should return a dictionary where the keys are dataset names and the values are dictionaries containing the best-performing model for each dataset, along with their types and features. The best-performing model is the one with the highest performance metric; if multiple models achieve the same highest performance for a dataset, the function should return the model with the lexicographically smallest name. The input dictionaries are structured as follows: `model_results` maps model names to dictionaries mapping dataset names to performance metrics, `model_types` maps model names to their types, and `datasets` maps dataset names to their corresponding features.
"""

def find_best_models(model_results, model_types, datasets):
    best_models = {}
    for dataset, results in model_results.items():
        best_model = min(results, key=lambda x: (-results[x], x))
        best_model_type = model_types[best_model]
        best_model_features = datasets[dataset]
        best_models[dataset] = {best_model: {'type': best_model_type, 'features': best_model_features}}
    return best_models