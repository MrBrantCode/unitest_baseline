"""
QUESTION:
Write a function `generate_weave_command` that generates a `weave` command to run a WordPress container with specific configurations. The function should take the following parameters: 
- `ip_address`: A string representing the IP address and subnet mask for the container's network.
- `db_host`: A string representing the IP address of the WordPress database host.
- `db_password`: A string representing the password for the WordPress database.
- `host_port`: An integer representing the port on the host machine to map to the container's port.
- `container_port`: An integer representing the port on which the WordPress container is running.
The function should return a string representing the `weave` command with the provided configurations.
"""

def generate_weave_command(ip_address, db_host, db_password, host_port, container_port):
    return f"sudo weave run {ip_address} -itd -e WORDPRESS_DB_HOST={db_host} -e WORDPRESS_DB_PASSWORD={db_password} -p {host_port}:{container_port} wordpress"