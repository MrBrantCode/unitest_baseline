"""
QUESTION:
Implement the function `estimate_channel_coefficients` to measure the channel for use in space-time coding schemes, given the I and Q streams from a receiver. The function should estimate the channel coefficients using known pilot symbols and return the complex conjugate of the estimated channel coefficients to 'reverse' the damage done by transmission. Assume the receiver is synchronized in time and frequency with the transmitter and the channel conditions are not rapidly changing.
"""

def estimate_channel_coefficients(pilot_symbols, received_pilot_symbols):
    """
    Estimates the channel coefficients using known pilot symbols and returns 
    the complex conjugate of the estimated channel coefficients.

    Parameters:
    pilot_symbols (list): The known pilot symbols.
    received_pilot_symbols (list): The received pilot symbols.

    Returns:
    list: The complex conjugate of the estimated channel coefficients.
    """
    # Initialize an empty list to store the estimated channel coefficients
    estimated_coefficients = []
    
    # Iterate over the pilot symbols and the received pilot symbols
    for pilot, received_pilot in zip(pilot_symbols, received_pilot_symbols):
        # Estimate the channel coefficient by dividing the received pilot symbol by the pilot symbol
        estimated_coefficient = received_pilot / pilot
        
        # Append the complex conjugate of the estimated coefficient to the list
        estimated_coefficients.append(estimated_coefficient.conjugate())
    
    return estimated_coefficients