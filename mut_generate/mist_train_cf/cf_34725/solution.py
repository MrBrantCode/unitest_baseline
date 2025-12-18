"""
QUESTION:
Write a function `extract_behavior_metrics` that takes a pandas DataFrame `dataframe` and a string `mouse_nickname` as input. The function should filter the dataframe to extract the data for the specified mouse nickname and return a dictionary containing the following behavioral metrics: `learned`, `date_learned`, `training_time`, `perf_easy`, `n_trials`, `threshold`, `bias`, `reaction_time`, `lapse_low`, and `lapse_high`. If the mouse data is not found, the function should return an empty dictionary.
"""

def extract_behavior_metrics(dataframe, mouse_nickname):
    mouse_data = dataframe[dataframe['mouse'] == mouse_nickname]
    if mouse_data.empty:
        return {}  

    metrics = {
        'learned': mouse_data['learned'].values[0],
        'date_learned': mouse_data['date_learned'].values[0],
        'training_time': mouse_data['training_time'].values[0],
        'perf_easy': mouse_data['perf_easy'].values[0],
        'n_trials': mouse_data['n_trials'].values[0],
        'threshold': mouse_data['threshold'].values[0],
        'bias': mouse_data['bias'].values[0],
        'reaction_time': mouse_data['reaction_time'].values[0],
        'lapse_low': mouse_data['lapse_low'].values[0],
        'lapse_high': mouse_data['lapse_high'].values[0]
    }
    return metrics