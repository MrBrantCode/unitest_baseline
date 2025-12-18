"""
QUESTION:
Create a function called `convert_addresses` that takes a string of addresses separated by commas as input. Each address consists of four components: street, city, state, and zip code, also separated by commas. The function should return a list of dictionaries, where each dictionary represents an address with keys 'street', 'city', 'state', and 'zip'.
"""

def convert_addresses(addresses):
    address_list = addresses.split(',')
    num_addresses = len(address_list) // 4
    result = []
    
    for i in range(num_addresses):
        start_index = i * 4
        address = {}
        address['street'] = address_list[start_index].strip()
        address['city'] = address_list[start_index + 1].strip()
        address['state'] = address_list[start_index + 2].strip()
        address['zip'] = address_list[start_index + 3].strip()
        result.append(address)
    
    return result