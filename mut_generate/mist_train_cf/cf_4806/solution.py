"""
QUESTION:
Create a function named `calculate_throughput` to calculate the network's throughput. The function should take five parameters: `data_rate` (in Mbps), `packet_size` (in bits), `efficiency_factor` (as a decimal), `error_rate` (as a decimal), and `max_allowable_delay` (in seconds). The input parameters should meet the following restrictions: `1 ≤ data_rate ≤ 100`, `500 ≤ packet_size ≤ 1500`, `0.7 ≤ efficiency_factor ≤ 0.9`, `0.0001 ≤ error_rate ≤ 0.001`, and `0.01 ≤ max_allowable_delay ≤ 0.1`.
"""

def calculate_throughput(data_rate, packet_size, efficiency_factor, error_rate, max_allowable_delay):
    if data_rate < 1 or data_rate > 100:
        return "Data rate should be between 1 Mbps and 100 Mbps."
    if packet_size < 500 or packet_size > 1500:
        return "Packet size should be between 500 bits and 1500 bits."
    if efficiency_factor < 0.7 or efficiency_factor > 0.9:
        return "Efficiency factor should be between 0.7 and 0.9."
    if error_rate < 0.0001 or error_rate > 0.001:
        return "Error rate should be between 0.01% and 0.1%."
    if max_allowable_delay < 0.01 or max_allowable_delay > 0.1:
        return "Maximum allowable delay should be between 10 milliseconds and 100 milliseconds."
    
    throughput = (data_rate * efficiency_factor * (1 - error_rate) * (1 - max_allowable_delay)) / (packet_size * 8)
    return throughput