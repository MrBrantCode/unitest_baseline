"""
QUESTION:
Implement a method `calculate_total_charge` in the `EventDataset` class that calculates the total charge of the events in the dataset. The method should take into account the `use_charge` attribute of the class, which determines whether to sum the charges directly or their absolute values. The `events` attribute is a list of dictionaries where each dictionary represents an event with a 'charge' key.

The `calculate_total_charge` method should return the total charge as a float. The class attributes `data_dir`, `data_key`, `knn`, `edge_weight`, `transform`, and `pre_transform` are not relevant to this method.
"""

def calculate_total_charge(events, use_charge: bool) -> float:
    """
    Calculate the total charge of the events.

    Args:
    events (list): A list of dictionaries where each dictionary represents an event with a 'charge' key.
    use_charge (bool): A flag to determine whether to sum the charges directly or their absolute values.

    Returns:
    float: The total charge of the events.
    """
    total_charge = 0
    for event in events:
        if use_charge:
            total_charge += event['charge']
        else:
            total_charge += abs(event['charge'])
    return total_charge