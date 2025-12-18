"""
QUESTION:
Write a function `process_email_list` that takes a list of email addresses as input and returns a dictionary where the keys are the unique email domains found in the list and the values are lists of unique email addresses from that domain. The email domains should be sorted in descending order based on the number of unique email addresses from that domain, and the email addresses within each domain should be sorted in descending order based on their length.
"""

def process_email_list(email_list):
    domain_dict = {}
    
    # Iterate through each email address in the list
    for email in email_list:
        # Extract the domain from the email address
        domain = email.split('@')[-1]
        
        # Add the email address to the domain's list
        if domain in domain_dict:
            domain_dict[domain].append(email)
        else:
            domain_dict[domain] = [email]
    
    # Sort the domains based on the number of unique email addresses
    sorted_domains = sorted(domain_dict.keys(), key=lambda x: len(set(domain_dict[x])), reverse=True)
    
    # Create a new dictionary with sorted domains and sorted email addresses within each domain
    sorted_dict = {}
    for domain in sorted_domains:
        # Remove duplicate email addresses within each domain
        unique_emails = list(set(domain_dict[domain]))
        # Sort the email addresses within each domain based on their length
        sorted_emails = sorted(unique_emails, key=lambda x: len(x), reverse=True)
        sorted_dict[domain] = sorted_emails
    
    return sorted_dict