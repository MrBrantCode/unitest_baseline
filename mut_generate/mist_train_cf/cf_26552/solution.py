"""
QUESTION:
Write a function named `calculate_starting_addresses` that takes an integer `num_regions` as input and calculates the starting addresses of memory regions based on a 4K aligned memory layout. The function should return a list of hexadecimal strings representing the starting addresses of the memory regions. The memory regions are 4K in size and the starting addresses should be aligned on 4K boundaries.
"""

def calculate_starting_addresses(num_regions):
    """Calculates the starting addresses of memory regions based on a 4K aligned memory layout."""
    
    # Initialize an empty list to store the starting addresses
    starting_addresses = []
    
    # Calculate the starting address of each memory region
    for i in range(num_regions):
        start_address = hex(i * 4096)  # Calculate the starting address based on 4K boundaries
        starting_addresses.append(start_address)
    
    # Return the list of starting addresses
    return starting_addresses