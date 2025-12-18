"""
QUESTION:
Write a function `average_datapoints_per_experiment` that takes a list of result rows as input, where each result row is a list containing a classifier name, RQ, experiment ID, iteration, number of datapoints, and number of features. The function should return a dictionary where the keys are tuples of (classifier name, experiment ID) and the values are the average number of datapoints for that classifier and experiment.
"""

def average_datapoints_per_experiment(result_rows):
    averages = {}
    counts = {}
    
    for row in result_rows:
        classifier_name, _, experiment_id, _, num_datapoints, _ = row
        key = (classifier_name, experiment_id)
        
        if key in averages:
            averages[key] = (averages[key] * counts[key] + num_datapoints) / (counts[key] + 1)
            counts[key] += 1
        else:
            averages[key] = num_datapoints
            counts[key] = 1
    
    return {key: averages[key] for key in averages}