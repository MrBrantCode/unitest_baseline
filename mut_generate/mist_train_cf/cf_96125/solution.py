"""
QUESTION:
Write a function `count_email_domains` that takes a list of email addresses as input and returns a dictionary where the keys are the unique domains and the values are the counts of unique email addresses in each domain. The domain is the part of the email address after the '@' symbol. If an email address appears multiple times in the input list, it should only be counted once in the output dictionary.
"""

def count_email_domains(emails):
    domain_counts = {}
    seen_emails = set()
    for email in emails:
        domain = email.split('@')[-1]
        if email not in seen_emails:
            seen_emails.add(email)
            if domain in domain_counts:
                domain_counts[domain] += 1
            else:
                domain_counts[domain] = 1
    return domain_counts