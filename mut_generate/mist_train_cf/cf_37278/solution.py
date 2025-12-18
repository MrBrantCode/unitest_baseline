"""
QUESTION:
Write a function `find_memory_devices` that takes a dictionary `devices_dict` representing memory devices and their specifications, and four parameters: `min_page_size`, `max_write_cycle`, `min_capacity`, and `required_bitmask`. The function should return a list of memory device keys that satisfy the following criteria: `page_size` is greater than or equal to `min_page_size`, `write_cycle` is less than or equal to `max_write_cycle`, `capacity` is greater than or equal to `min_capacity`, and `bitmask` matches `required_bitmask`. The function should return an empty list if no devices meet the criteria.
"""

def find_memory_devices(devices_dict, min_page_size, max_write_cycle, min_capacity, required_bitmask):
    matching_devices = []
    for key, specs in devices_dict.items():
        if (specs["page_size"] >= min_page_size and
            specs["write_cycle"] <= max_write_cycle and
            specs["capacity"] >= min_capacity and
            specs["bitmask"] == required_bitmask):
            matching_devices.append(key)
    return matching_devices