"""
QUESTION:
Write a function named `domain_emails` that takes a list of email addresses as input and returns a dictionary. The dictionary's keys should be the unique email domains found in the list, and the values should be lists of email addresses from that domain. The email domains should be sorted in ascending order, and the email addresses within each domain should be sorted in descending order based on their length.
"""

def domain_emails(emails):
    domain_dict = {}
    
    for email in emails:
        domain = email.split('@')[1]
        if domain not in domain_dict:
            domain_dict[domain] = []
        domain_dict[domain].append(email)
    
    for domain in domain_dict:
        domain_dict[domain].sort(key=len, reverse=True)
    
    return {domain: sorted(emails) for domain, emails in sorted(domain_dict.items())}