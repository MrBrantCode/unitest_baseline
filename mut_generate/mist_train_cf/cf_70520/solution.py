"""
QUESTION:
Design a function named `nebula_graph_config` that configures communication between Spark (running outside a container network) and NebulaGraph (operating inside a container network). The function should account for exposing NebulaGraph services, hostname resolution, network configuration, and updating Spark Connector configuration to establish clear communication paths between Spark and NebulaGraph containers in different network environments.
"""

def nebula_graph_config(nebula_address_graph, nebula_address_meta, spark_address, metad_http_port):
    """
    Configures communication between Spark and NebulaGraph by exposing NebulaGraph services, 
    handling hostname resolution, network configuration, and updating Spark Connector configuration.

    Args:
        nebula_address_graph (str): The accessible IP address of NebulaGraph graph service.
        nebula_address_meta (str): The accessible IP address of NebulaGraph meta service.
        spark_address (str): The IP address of the Spark service.
        metad_http_port (int): The HTTP port of the metad service.

    Returns:
        dict: A dictionary containing the updated configuration for Spark Connector.
    """

    # Expose NebulaGraph Services
    # Assuming we are using Docker with port mapping
    # This step is usually done when starting the container
    # For example: docker run -p <host_port>:<container_port> ...

    # Hostname Resolution
    # This can be managed through /etc/hosts or a DNS server
    # For simplicity, we assume this is already handled

    # Network Configuration
    # Update the metad's --ws_meta_http_port to the actual IP and port
    # This is usually done in the nebula-metad.conf file
    # For simplicity, we assume this is already handled

    # Update Spark Connector Configuration
    # Provide the accessible IP address and port in nebula.address.graph and nebula.address.meta
    config = {
        'nebula.address.graph': nebula_address_graph,
        'nebula.address.meta': nebula_address_meta,
        'spark.address': spark_address,
        'metad.http.port': metad_http_port
    }

    return config