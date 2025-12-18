"""
QUESTION:
Write a function called `numUniqueEmails(emails)` that takes a list of email addresses as input and returns the number of unique email addresses that would actually receive mail along with the most common domain name in the list. The input list contains strings of lowercase English letters, '+', '.', and '@'. Each string has exactly one '@' character, and local names do not start with a '+' character. The function should normalize the email addresses by ignoring '.' characters and everything after the first '+' in the local name, and then count the unique normalized addresses and the most common domain name.
"""

def numUniqueEmails(emails):
    unique_emails = set()
    domain_count = {}
    most_common_domain = ""
    max_count = 0

    for email in emails:
        local_name, domain_name = email.split("@")
        
        # Remove everything after '+' in local name
        local_name = local_name.split("+")[0].replace('.', '')
        
        # Append '@' to the local name and the domain name
        normalized_email = local_name + "@" + domain_name
        
        # Add to the set of unique emails
        unique_emails.add(normalized_email)
        
        # Increment the count for the domain
        domain_count[domain_name] = domain_count.get(domain_name, 0) + 1
        
        # Update most common domain if necessary
        if domain_count[domain_name] > max_count:
            max_count = domain_count[domain_name]
            most_common_domain = domain_name
    
    return len(unique_emails), most_common_domain