"""
QUESTION:
Implement the `manage_static_routes` function, which takes in three parameters: `current_static_routes`, `last_static_routes`, and `deleted_routes`. The function should perform the following actions:

- Add any new static routes from `last_static_routes` to `current_static_routes`.
- Remove any routes specified in `deleted_routes` from `current_static_routes`.
- Update any routes in `current_static_routes` that have been modified in `last_static_routes`.

`current_static_routes` and `last_static_routes` are dictionaries representing static routes, where the keys are network IDs and the values are lists of tuples in the format `(CIDR, destination_network_id)`. `deleted_routes` is a list of tuples representing the routes that need to be deleted, each containing the source network ID, the CIDR, and the destination network ID.

The function should return the updated `current_static_routes` after performing the necessary operations.
"""

def manage_static_routes(current_static_routes, last_static_routes, deleted_routes):
    # Add new static routes from last_static_routes to current_static_routes
    for network_id, routes in last_static_routes.items():
        if network_id not in current_static_routes:
            current_static_routes[network_id] = routes
        else:
            for cidr, dest_network_id in routes:
                if (cidr, dest_network_id) not in current_static_routes[network_id]:
                    current_static_routes[network_id].append((cidr, dest_network_id))

    # Remove routes specified in deleted_routes from current_static_routes
    for source_network_id, cidr, dest_network_id in deleted_routes:
        if source_network_id in current_static_routes:
            current_static_routes[source_network_id] = [(c, d) for c, d in current_static_routes[source_network_id] if (c, d) != (cidr, dest_network_id)]

    # Update routes in current_static_routes that have been modified in last_static_routes
    for network_id, routes in last_static_routes.items():
        if network_id in current_static_routes:
            for cidr, dest_network_id in routes:
                if (cidr, dest_network_id) in current_static_routes[network_id]:
                    current_static_routes[network_id] = [(c, d) for c, d in current_static_routes[network_id] if (c, d) != (cidr, dest_network_id)]
                    current_static_routes[network_id].append((cidr, dest_network_id))

    return current_static_routes