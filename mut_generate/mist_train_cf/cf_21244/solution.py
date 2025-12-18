"""
QUESTION:
Write a function called `extract_email_domains(paragraph)` that takes a string `paragraph` as input, extracts valid email addresses from the paragraph, identifies the domain names from these email addresses, and returns a list of tuples containing the domain names and their respective occurrence counts in descending order. The function should consider domain names as case-insensitive and only extract valid email addresses containing an "@" symbol and a domain name.
"""

import re
from collections import Counter

def extract_email_domains(paragraph):
    # Extract email addresses from the paragraph
    email_regex = r'[\w\.-]+@[\w\.-]+'
    email_addresses = re.findall(email_regex, paragraph)
    
    # Extract domain names from email addresses
    domain_names = [email.split('@')[1].lower() for email in email_addresses]
    
    # Count the occurrences of each domain name
    domain_counts = Counter(domain_names)
    
    # Sort domain names in descending order of occurrence counts
    sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_domains