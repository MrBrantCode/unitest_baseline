"""
QUESTION:
Write a Python function `packet_reassembly` that demonstrates how IP protocol reassembles fragmented packets at the destination host, given a list of packets with their corresponding sequence numbers and data. The function should take as input a list of dictionaries, where each dictionary contains 'packet_id', 'sequence_number', and 'data'. The function should return the reassembled data as a string.
"""

def packet_reassembly(packets):
    """
    Reassembles fragmented packets at the destination host.

    Args:
    packets (list): A list of dictionaries, where each dictionary contains 'packet_id', 'sequence_number', and 'data'.

    Returns:
    str: The reassembled data as a string.
    """
    
    # Sort the packets based on their sequence numbers
    packets.sort(key=lambda x: x['sequence_number'])
    
    # Initialize an empty string to store the reassembled data
    reassembled_data = ''
    
    # Iterate over the sorted packets and append their data to the reassembled data
    for packet in packets:
        reassembled_data += packet['data']
    
    return reassembled_data