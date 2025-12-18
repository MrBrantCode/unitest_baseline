"""
QUESTION:
Implement the `compute_aggregate_metric_ops` function, which takes in a dictionary `metric_ops`, a list of module names `module_names`, and a dictionary of model parameters `model_params`. The function should return a list of aggregated metrics and a list of operations based on the model's configuration. The function should add the metric operation 'boundary/f1' from `metric_ops` to the aggregated metrics if 'boundary' is in `module_names` and `boundary_weight` in `model_params` is greater than 0. The function should return the aggregated metrics and operations.
"""

def compute_aggregate_metric_ops(metric_ops, module_names, model_params):
    metrics = []
    ops = []
    if 'boundary' in module_names and model_params.get('boundary_weight', 0) > 0:
        metrics.append(metric_ops.get('boundary/f1', None))
    return metrics, ops