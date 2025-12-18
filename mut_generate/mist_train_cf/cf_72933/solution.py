"""
QUESTION:
Create a function `organize_and_count(emails)` that takes a list of email addresses as input, categorizes them by domain and service provider, and returns the count of emails for each domain and service provider. The function should consider subdomains as part of the domain name, and map domains to their corresponding service providers using a predefined dictionary. The function should return the counts in a program-readable format.
"""

from collections import Counter

def get_domain(email):
    return email.split('@')[1]

def get_service_provider(domain):
    domain_to_service_provider = {
        'gmail.com': 'Google',
        'mail.google.com': 'Google',
        'yahoo.com': 'Yahoo',
        'hotmail.com': 'Microsoft',
        'outlook.com': 'Microsoft',
        # add more domain-service provider mappings here as needed...
    }
    return domain_to_service_provider.get(domain, 'Unknown')

def organize_and_count(emails):
    domains = [get_domain(email) for email in emails]
    service_providers = [get_service_provider(domain) for domain in domains]
    
    domain_counts = dict(Counter(domains))
    service_provider_counts = dict(Counter(service_providers))
    
    return domain_counts, service_provider_counts