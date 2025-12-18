"""
QUESTION:
Create a function `degradation_percent` that calculates the degradation percentage of network interfaces based on the historical data and the current LLDP information. The function takes two parameters: `total_interfaces` (the total number of network interfaces in the system) and `current_lldp_interfaces` (a list containing the currently active interfaces obtained from LLDP). The function should update the global variable `good_history_uplink` (a list of previously known good interfaces) with the new `total_interfaces` and then calculate the percentage of interfaces that are no longer active compared to the historical data. The function should return the result as a floating-point number rounded to two decimal places.

Note: The global variable `good_history_uplink` will be provided and used to store historical data.
"""

def degradation_percent(total_interfaces, current_lldp_interfaces):
    global good_history_uplink
    good_history_uplink = list(OrderedDict.fromkeys(good_history_uplink + list(range(1, total_interfaces + 1))))
    total_interfaces_len = len(good_history_uplink)
    uplink_down_list = [intf for intf in good_history_uplink if intf not in current_lldp_interfaces]
    uplink_down_length = len(uplink_down_list)
    if total_interfaces_len == 0:
        return 0.0
    else:
        degradation_percentage = (uplink_down_length / total_interfaces_len) * 100
        return round(degradation_percentage, 2)