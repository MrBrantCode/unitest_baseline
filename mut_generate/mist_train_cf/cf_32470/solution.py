"""
QUESTION:
Write a function `update_service_distribution` that takes in two parameters: `prior_distribution` and `updated_profile`, both lists of services, where a service can be any hashable object. The function should return a list representing the updated service distribution, reusing services from `prior_distribution` whenever possible, and incorporating the updated services from `updated_profile`. The order of services in `prior_distribution` should be maintained for the services that are reused.
"""

def update_service_distribution(prior_distribution, updated_profile):
    existing_services = set(prior_distribution)
    updated_distribution = list(existing_services)  # Reuse existing services

    for service in updated_profile:
        if service in existing_services:
            continue  # Reuse existing service
        else:
            updated_distribution.append(service)  # Add updated service to the distribution

    return updated_distribution