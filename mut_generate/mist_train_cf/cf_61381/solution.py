"""
QUESTION:
Implement a function named `queue_system` to model a vehicle arrival queue system at a traffic light where vehicles arrive in chunks due to the green/red phases of upstream traffic lights. The function should consider parameters such as arrival rate, service rate, batch size, and traffic intensity to determine the best suited probability distribution for the scenario, which can be a Markov-modulated Poisson process, Bernoulli splitting models, or a Batch Markovian Arrival Process.
"""

def queue_system(arrival_rate, service_rate, batch_size, traffic_intensity, batch_distribution='poisson', 
                 state_transition_matrix=None):
    """
    Model a vehicle arrival queue system at a traffic light.

    Parameters:
    arrival_rate (float): The average number of vehicles arriving at the traffic light per unit of time.
    service_rate (float): The rate at which vehicles pass the traffic light.
    batch_size (int): The size of each batch of vehicles arriving at the traffic light.
    traffic_intensity (float): The ratio of the arrival rate to the service rate.
    batch_distribution (str): The distribution of batch sizes. Defaults to 'poisson'.
    state_transition_matrix (numpy array): The state transition matrix for BMAP models. Defaults to None.

    Returns:
    dict: A dictionary containing the key parameters of the queue system.
    """
    queue_system_parameters = {
        'arrival_rate': arrival_rate,
        'service_rate': service_rate,
        'batch_size': batch_size,
        'traffic_intensity': traffic_intensity,
        'batch_distribution': batch_distribution
    }
    
    if state_transition_matrix is not None:
        queue_system_parameters['state_transition_matrix'] = state_transition_matrix
    
    return queue_system_parameters