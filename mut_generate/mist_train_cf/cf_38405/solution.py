"""
QUESTION:
Implement a function `manage_dhcp_options` that takes three boolean parameters: `delete_dhcp_options`, `purge_dhcp_options`, and a string parameter `state` with possible values 'create', 'update', or 'delete'. The function should return a message indicating the success or failure of the operation based on the input parameters. If `delete_dhcp_options` and `purge_dhcp_options` are both true, or if the `state` is not one of 'create', 'update', or 'delete', the function should return an error message.
"""

def manage_dhcp_options(delete_dhcp_options, purge_dhcp_options, state):
    if delete_dhcp_options and purge_dhcp_options:
        return "Error: delete_dhcp_options and purge_dhcp_options are mutually exclusive."

    if state not in ['create', 'update', 'delete']:
        return "Error: Invalid state. State should be 'create', 'update', or 'delete'."

    if delete_dhcp_options:
        return "DHCP options deleted successfully."

    if purge_dhcp_options:
        return "DHCP options purged successfully."

    # Handle create or update state
    # Implement logic to create or update DHCP options

    return "DHCP options created/updated successfully."