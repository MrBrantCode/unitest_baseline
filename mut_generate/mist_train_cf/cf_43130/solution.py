"""
QUESTION:
Implement a function `calculate_total_channel_capacity` that takes in a `network_state` object and a `token_network_address` as parameters. The function should return the total capacity of all open Netting channels for the given `token_network_address` in the Raiden network. The `network_state` object contains information about the current state of the network, including the channels and their respective states. The function should only consider channels that are in an 'open' state and have a matching `token_network_address`.
"""

def calculate_total_channel_capacity(network_state, token_network_address):
    total_capacity = 0
    if token_network_address in network_state.channels_to_nested.values():
        for channels in network_state.channels_to_nested.values():
            for channel in channels.values():
                if channel.token_network_address == token_network_address and channel.state == 'open':
                    total_capacity += channel.balance_proof.capacity
    return total_capacity