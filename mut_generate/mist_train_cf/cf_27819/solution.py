"""
QUESTION:
Implement the `map_waypoint_name_to_number` function that maps waypoint identifiers to names based on the odometry vertices. The function should take no parameters and return nothing. The mapping should start from the next available ID after the highest odometry vertex ID, and the names should be assigned in ascending order based on the waypoint IDs. The name format should be "Waypoint_X", where X is the assigned ID. The function should use the given instance variables `waypoints_vertices`, `odometry_vertices`, `waypoint_id_to_name`, and `waypoint_start_id`.
"""

def map_waypoint_name_to_number(waypoints_vertices, odometry_vertices, waypoint_id_to_name, waypoint_start_id):
    waypoint_id_to_name.clear()
    waypoint_start_id = max(odometry_vertices.keys()) + 1
    sorted_waypoint_ids = sorted(waypoints_vertices.keys())
    for i, waypoint_id in enumerate(sorted_waypoint_ids):
        waypoint_id_to_name[waypoint_id] = f"Waypoint_{waypoint_start_id + i}"
    return waypoint_id_to_name