"""
QUESTION:
Create a function called `parse_server_xml` that takes an XML file path as input, reads the XML file, and performs the following operations: 
For each server with 'active' status, print its name and IP address. 
Count the total number of servers with 'inactive' status. 
The function should use the ElementTree module for XML parsing and should not take any other arguments.
"""

import xml.etree.ElementTree as ET

def parse_server_xml(xml_file):
    """
    Parse an XML file containing server information and perform operations based on server status.

    Args:
        xml_file (str): Path to the XML file.

    Returns:
        int: Total number of inactive servers.
    """
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    inactive_servers_count = 0

    # Iterate through the server elements
    for server in root.findall('server'):
        name = server.find('name').text
        ip = server.find('ip').text
        status = server.find('status').text

        if status == 'active':
            print(f"Active Server - Name: {name}, IP: {ip}")
        elif status == 'inactive':
            inactive_servers_count += 1

    print(f"Total inactive servers: {inactive_servers_count}")
    return inactive_servers_count