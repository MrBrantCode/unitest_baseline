"""
QUESTION:
Design a Service Oriented Architecture (SOA) to provide end-client independent access to various processes and make data available offline. The SOA should be designed to avoid common pitfalls such as coarse-grained or fine-grained services, underestimating design and governance, and insufficient security measures. Define a strategy for implementing secure authentication, authorization, confidentiality, and availability, including message-level security using protocols like WS-Security. Determine the appropriate level of service granularity based on the type of process being enabled.
"""

def service_oriented_architecture(service_type, process_type):
    """
    A function representing a service-oriented architecture.

    Args:
    service_type (str): The type of service.
    process_type (str): The type of process the service is meant to enable.

    Returns:
    dict: A dictionary containing the service type and process type.
    """
    # Implement the service-oriented architecture logic here
    # For example, determine the level of service granularity based on the type of process
    if process_type == "coarse-grained":
        granularity = "high"
    elif process_type == "fine-grained":
        granularity = "low"
    else:
        granularity = "medium"

    # Return the service type and process type
    return {"service_type": service_type, "process_type": process_type, "granularity": granularity}