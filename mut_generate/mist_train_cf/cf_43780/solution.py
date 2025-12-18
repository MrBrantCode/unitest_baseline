"""
QUESTION:
Write a function `topDelayedStates` that takes two tables, `delayedFlights` and `airport`, as input. The function should return the top 5 distinct states in which a flight between different airports within the same state has been delayed (either in arrival or departure) by descending order with respect to the number of such delays. The function should join the `delayedFlights` table with the `airport` table twice to match flights that both departed and arrived at airports in the same state, and only consider flights with delays. 

Restrictions: The `delayedFlights` table has columns for flight information, and the `airport` table has columns for airport information including the state.
"""

def topDelayedStates(delayedFlights, airport):
    # Perform a self join on the `delayedFlights` table to match flights that both departed and arrived at airports in the same state
    delayedFlights = delayedFlights.merge(airport[['iata', 'state']].rename(columns={'iata': 'src'}), left_on='src', right_on='src')
    delayedFlights = delayedFlights.merge(airport[['iata', 'state']].rename(columns={'iata': 'dest'}), left_on='dest', right_on='dest')
    
    # Only consider flights that have been delayed
    delayedFlights = delayedFlights[(delayedFlights['dep_delay'] > 0) | (delayedFlights['arr_delay'] > 0)]
    
    # Only consider flights within the same state
    delayedFlights = delayedFlights[delayedFlights['state_x'] == delayedFlights['state_y']]
    
    # Count the number of such delays per state
    state_delays = delayedFlights['state_x'].value_counts()
    
    # Return the top 5 states
    return state_delays.nlargest(5)