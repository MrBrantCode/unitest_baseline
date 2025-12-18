"""
QUESTION:
Develop a function called `categorize_emails` that takes a list of email addresses as input and returns a dictionary where the keys are the email domains and the values are lists of email addresses from the input list sorted first by character count and then alphabetically in case of a tie.
"""

from collections import defaultdict

def categorize_emails(emails):
  """
  This function categorizes a list of email addresses by their domains.
  The emails within each domain are sorted first by character count and then alphabetically in case of a tie.

  Args:
    emails (list): A list of email addresses.

  Returns:
    dict: A dictionary where the keys are the email domains and the values are lists of email addresses.
  """

  # Sort the emails first by length, then alphabetically
  emails.sort(key=lambda x: (len(x), x))

  # Separate emails based on their domain
  domains = defaultdict(list)
  for email in emails:
    domain = email.split("@")[-1]
    domains[domain].append(email)

  return domains